#!/usr/bin/env python3
"""
Select ~1000 well-connected notes from ~/Laputa for demo vault.
Build link graph, prioritize well-connected notes with good frontmatter.
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict, Counter
import shutil

LAPUTA_ROOT = Path.home() / "Laputa"
DEMO_ROOT = Path.home() / "Workspace" / "laputa-app" / "demo-vault"

# Categories to include (skip journal)
INCLUDE_CATEGORIES = [
    'essay', 'evergreen', 'note', 'project', 'experiment', 'procedure',
    'responsibility', 'event', 'person', 'topic', 'quarter', 'month',
    'measure', 'target', 'goal', 'key-result', 'area', 'monday-ideas',
    'readings', 'readings-digest', 'resource', 'movie', 'video', 'tv-show',
    'hotel', 'restaurant', 'year', 'vital', 'buckets'
]

# Target distribution (rough proportions for ~1000 notes)
TARGET_DIST = {
    'procedure': 45,      # all
    'responsibility': 30, # all
    'month': 42,          # all
    'quarter': 30,        # all
    'year': 7,            # all
    'topic': 70,          # most
    'project': 150,       # most
    'person': 150,        # sample
    'essay': 150,         # sample
    'evergreen': 150,     # sample
    'note': 100,          # sample
    'event': 80,          # selective
    'goal': 50,           # selective
    'key-result': 50,     # selective
}

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---\n'):
        return {}
    
    try:
        end = content.index('\n---\n', 4)
        fm_text = content[4:end]
        return yaml.safe_load(fm_text) or {}
    except (ValueError, yaml.YAMLError):
        return {}

def extract_wikilinks(content):
    """Extract all [[wikilinks]] from content."""
    # Match [[target]] or [[target|alias]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = [m.group(1) for m in re.finditer(pattern, content)]
    # Clean up links: remove .md extension if present
    return [link.replace('.md', '') for link in links]

def score_frontmatter(fm):
    """Score frontmatter quality (0-3)."""
    score = 0
    if fm.get('Is A'):
        score += 1
    if fm.get('Belongs to'):
        score += 1
    if fm.get('Related to'):
        score += 1
    return score

def get_category(path):
    """Get category from path."""
    rel = path.relative_to(LAPUTA_ROOT)
    return rel.parts[0] if len(rel.parts) > 1 else 'root'

def build_graph():
    """Scan all notes, build link graph, return node data."""
    print("📊 Scanning notes and building link graph...")
    
    nodes = {}  # path -> {title, category, fm_score, outlinks, inlinks}
    link_lookup = {}  # Multiple ways to reference a note: title, folder/title, relative path
    
    # First pass: collect all notes
    for md_file in LAPUTA_ROOT.rglob("*.md"):
        # Skip journal
        if '/journal/' in str(md_file):
            continue
        
        category = get_category(md_file)
        if category not in INCLUDE_CATEGORIES:
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"⚠️  Skip {md_file}: {e}")
            continue
        
        fm = extract_frontmatter(content)
        wikilinks = extract_wikilinks(content)
        title = md_file.stem
        rel_path = str(md_file.relative_to(LAPUTA_ROOT).with_suffix(''))
        
        nodes[md_file] = {
            'title': title,
            'category': category,
            'fm_score': score_frontmatter(fm),
            'outlinks': wikilinks,
            'inlinks': [],
            'content_length': len(content),
            'rel_path': rel_path
        }
        
        # Register multiple ways to reference this note
        link_lookup[title] = md_file  # Just filename
        link_lookup[rel_path] = md_file  # Full relative path
        link_lookup[f"{category}/{title}"] = md_file  # category/title
    
    print(f"✅ Found {len(nodes)} notes (excluding journal)")
    
    # Second pass: resolve links and build inlink graph
    print("🔗 Resolving wikilinks...")
    for path, node in nodes.items():
        for link_ref in node['outlinks']:
            if link_ref in link_lookup:
                target_path = link_lookup[link_ref]
                if target_path in nodes:
                    nodes[target_path]['inlinks'].append(path)
    
    # Calculate connection scores
    for path, node in nodes.items():
        node['out_degree'] = len(node['outlinks'])
        node['in_degree'] = len(node['inlinks'])
        node['total_degree'] = node['out_degree'] + node['in_degree']
    
    return nodes, link_lookup

def select_notes(nodes, link_lookup, target_count=1000):
    """Select ~target_count notes prioritizing connectivity."""
    print(f"\n🎯 Selecting ~{target_count} notes...")
    
    # Group by category
    by_category = defaultdict(list)
    for path, node in nodes.items():
        by_category[node['category']].append(path)
    
    selected = set()
    
    # Phase 1: Include all from small important categories
    priority_cats = ['procedure', 'responsibility', 'month', 'quarter', 'year', 'area']
    for cat in priority_cats:
        if cat in by_category:
            selected.update(by_category[cat])
            print(f"  ✓ {cat}: {len(by_category[cat])} (all)")
    
    print(f"  Phase 1: {len(selected)} notes selected")
    
    # Phase 2: Sample from other categories by connectivity
    remaining_target = target_count - len(selected)
    remaining_cats = [c for c in INCLUDE_CATEGORIES if c not in priority_cats]
    
    # Score and rank all remaining notes
    candidates = []
    for cat in remaining_cats:
        for path in by_category[cat]:
            if path not in selected:
                node = nodes[path]
                # Score = connectivity + frontmatter quality
                score = node['total_degree'] * 10 + node['fm_score']
                candidates.append((score, path))
    
    candidates.sort(reverse=True)
    
    # Take top N, but ensure category diversity
    cat_counts = Counter()
    for score, path in candidates:
        if len(selected) >= target_count:
            break
        
        cat = nodes[path]['category']
        cat_limit = TARGET_DIST.get(cat, 50)
        
        if cat_counts[cat] < cat_limit:
            selected.add(path)
            cat_counts[cat] += 1
    
    print(f"  Phase 2: {len(selected)} total notes selected")
    
    # Phase 3: Expand by following links to improve coherence
    print("  Phase 3: Expanding to improve link coherence...")
    iteration = 0
    prev_resolution = 0
    
    while len(selected) < target_count * 2.0:  # Allow 100% overage for link coherence
        iteration += 1
        if iteration > 15:
            break
        
        # Calculate current link resolution
        total_links = 0
        resolved_links = 0
        for path in selected:
            node = nodes[path]
            for link_ref in node['outlinks']:
                total_links += 1
                if link_ref in link_lookup:
                    target = link_lookup[link_ref]
                    if target in selected:
                        resolved_links += 1
        
        current_resolution = resolved_links / total_links if total_links > 0 else 0
        
        # Stop if we hit 80% resolution
        if current_resolution >= 0.80:
            print(f"    ✅ Reached {current_resolution:.1%} link resolution!")
            break
        
        # Find most frequently linked-to notes not yet in selection
        external_refs = Counter()
        for path in selected:
            node = nodes[path]
            for link_ref in node['outlinks']:
                if link_ref in link_lookup:
                    target_path = link_lookup[link_ref]
                    if target_path in nodes and target_path not in selected:
                        external_refs[target_path] += 1
        
        if not external_refs:
            break
        
        # Add top referenced notes (be more generous with limits)
        added = 0
        # Lower threshold as iterations progress
        min_refs = max(1, 3 - iteration // 2)
        
        for path, count in external_refs.most_common(200):
            if len(selected) >= target_count * 2.0:
                break
            if count < min_refs:
                continue
            
            cat = nodes[path]['category']
            cat_limit = TARGET_DIST.get(cat, 50)
            # Very generous limits for link coherence
            max_cat_size = max(cat_limit * 3.0, 100)
            if cat_counts[cat] < max_cat_size:
                selected.add(path)
                cat_counts[cat] += 1
                added += 1
        
        print(f"    Iteration {iteration}: added {added} notes (total: {len(selected)}, resolution: {current_resolution:.1%})")
        
        if added == 0:
            break
    
    # Final category breakdown
    print("\n📊 Final selection by category:")
    final_counts = Counter(nodes[p]['category'] for p in selected)
    for cat, count in sorted(final_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")
    
    return selected

def verify_link_coherence(nodes, selected, link_lookup):
    """Check link resolution rate in selected set."""
    print("\n🔗 Verifying link coherence...")
    
    # Build set of all possible references to selected notes
    selected_refs = set()
    for path in selected:
        node = nodes[path]
        selected_refs.add(node['title'])
        selected_refs.add(node['rel_path'])
        selected_refs.add(f"{node['category']}/{node['title']}")
    
    total_links = 0
    resolved_links = 0
    broken_by_note = []
    
    for path in selected:
        node = nodes[path]
        outlinks = node['outlinks']
        total_links += len(outlinks)
        
        resolved = 0
        for link in outlinks:
            if link in link_lookup:
                target = link_lookup[link]
                if target in selected:
                    resolved += 1
        
        resolved_links += resolved
        
        if outlinks:
            resolution_rate = resolved / len(outlinks)
            if resolution_rate < 0.5 and len(outlinks) > 3:
                broken_by_note.append((path, resolution_rate, len(outlinks), resolved))
    
    overall_rate = resolved_links / total_links if total_links > 0 else 0
    
    print(f"  Total outgoing links: {total_links}")
    print(f"  Resolved links: {resolved_links}")
    print(f"  Resolution rate: {overall_rate:.1%}")
    
    if broken_by_note:
        print(f"\n  ⚠️  {len(broken_by_note)} notes with <50% link resolution and >3 links:")
        for path, rate, total, resolved in sorted(broken_by_note, key=lambda x: x[1])[:10]:
            print(f"    {nodes[path]['category']}/{nodes[path]['title']}: {resolved}/{total} ({rate:.0%})")
    
    return overall_rate

def copy_selected_notes(selected, nodes):
    """Copy selected notes to demo vault, maintaining structure."""
    print(f"\n📂 Copying {len(selected)} notes to {DEMO_ROOT}...")
    
    # Clean and create demo root
    if DEMO_ROOT.exists():
        print(f"  Removing existing {DEMO_ROOT}")
        shutil.rmtree(DEMO_ROOT)
    
    DEMO_ROOT.mkdir(parents=True, exist_ok=True)
    
    copied = 0
    errors = []
    
    for path in selected:
        rel_path = path.relative_to(LAPUTA_ROOT)
        dest = DEMO_ROOT / rel_path
        
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)
            copied += 1
        except Exception as e:
            errors.append((path, e))
    
    print(f"  ✅ Copied {copied} notes")
    
    if errors:
        print(f"  ⚠️  {len(errors)} errors:")
        for path, err in errors[:5]:
            print(f"    {path}: {err}")
    
    return copied

def main():
    print("🚀 Creating Laputa demo vault\n")
    
    # Build graph
    nodes, link_lookup = build_graph()
    
    # Select notes
    selected = select_notes(nodes, link_lookup, target_count=1000)
    
    # Verify coherence
    link_resolution = verify_link_coherence(nodes, selected, link_lookup)
    
    # Copy files
    copied = copy_selected_notes(selected, nodes)
    
    # Final report
    print("\n" + "="*60)
    print("✅ DEMO VAULT CREATED")
    print("="*60)
    print(f"Total notes: {copied}")
    print(f"Link resolution: {link_resolution:.1%}")
    print(f"Location: {DEMO_ROOT}")
    
    return link_resolution >= 0.80

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
