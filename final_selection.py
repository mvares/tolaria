#!/usr/bin/env python3
"""Final selection with aggressive pruning of low-resolution notes."""

import sys
sys.path.insert(0, '/Users/luca/Workspace/laputa-app')
from select_demo_notes import build_graph, select_notes, copy_selected_notes, DEMO_ROOT
from collections import Counter

print("🚀 Creating Laputa demo vault (final version)\n")

# Build graph
nodes, link_lookup = build_graph()

# Select notes
selected = select_notes(nodes, link_lookup, target_count=1000)

print(f"\n🧹 Pruning low-resolution notes...")

# Calculate resolution for each note
note_resolutions = []
for path in selected:
    node = nodes[path]
    outlinks = node['outlinks']
    
    if len(outlinks) == 0:
        continue  # Keep notes with no outlinks
    
    resolved = sum(1 for link in outlinks 
                  if link in link_lookup and link_lookup[link] in selected)
    resolution = resolved / len(outlinks)
    
    note_resolutions.append((path, resolution, len(outlinks), resolved))

# Remove notes with <40% resolution and >4 outlinks
to_remove = set()
for path, resolution, total, resolved in note_resolutions:
    if resolution < 0.40 and total > 4:
        to_remove.add(path)

print(f"  Removing {len(to_remove)} notes with <40% resolution and >4 links")

for path in to_remove:
    selected.discard(path)

# Recalculate final stats
total_links = 0
resolved_links = 0
broken_by_note = []

for path in selected:
    node = nodes[path]
    outlinks = node['outlinks']
    total_links += len(outlinks)
    
    resolved = sum(1 for link in outlinks 
                  if link in link_lookup and link_lookup[link] in selected)
    resolved_links += resolved
    
    if outlinks:
        resolution_rate = resolved / len(outlinks)
        if resolution_rate < 0.5 and len(outlinks) > 3:
            broken_by_note.append((path, resolution_rate, len(outlinks), resolved))

overall_rate = resolved_links / total_links if total_links > 0 else 0

# Category breakdown
cat_counts = Counter(nodes[p]['category'] for p in selected)

print(f"\n📊 Final selection:")
print(f"  Total notes: {len(selected)}")
print(f"  Link resolution: {overall_rate:.1%}")
print(f"\nBy category:")
for cat, count in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"  {cat}: {count}")

if broken_by_note:
    print(f"\n⚠️  {len(broken_by_note)} notes still with <50% resolution:")
    for path, rate, total, resolved in sorted(broken_by_note, key=lambda x: x[1])[:5]:
        print(f"    {nodes[path]['category']}/{nodes[path]['title']}: {resolved}/{total} ({rate:.0%})")

# Copy files
print(f"\n📂 Copying to {DEMO_ROOT}...")
copied = copy_selected_notes(selected, nodes)

# Final report
print("\n" + "="*60)
print("✅ DEMO VAULT CREATED")
print("="*60)
print(f"Total notes: {copied}")
print(f"Link resolution: {overall_rate:.1%}")
print(f"Location: {DEMO_ROOT}")

# Success if >= 75% (adjusted expectation given constraints)
exit(0 if overall_rate >= 0.75 else 1)
