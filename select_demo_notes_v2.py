#!/usr/bin/env python3
"""
Select ~1000 well-connected notes from ~/Laputa for demo vault.
V2: Also prune notes with too many dead links.
"""

import sys
sys.path.insert(0, '/Users/luca/Workspace/laputa-app')
from select_demo_notes import (
    build_graph, select_notes, copy_selected_notes,
    DEMO_ROOT, LAPUTA_ROOT
)

def prune_dead_link_notes(nodes, selected, link_lookup):
    """Remove notes with too many links to non-existent notes."""
    print("\n🧹 Pruning notes with excessive dead links...")
    
    to_remove = set()
    
    for path in selected:
        node = nodes[path]
        outlinks = node['outlinks']
        
        if len(outlinks) < 4:  # Don't prune notes with few links
            continue
        
        dead_links = 0
        for link_ref in outlinks:
            if link_ref not in link_lookup:
                dead_links += 1
        
        dead_ratio = dead_links / len(outlinks) if outlinks else 0
        
        # Remove if >40% dead links and >3 total links
        if dead_ratio > 0.4 and dead_links > 2:
            to_remove.add(path)
    
    if to_remove:
        print(f"  Removing {len(to_remove)} notes with excessive dead links")
        for path in to_remove:
            selected.discard(path)
    
    return selected

def verify_final_resolution(nodes, selected, link_lookup):
    """Final link resolution check."""
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
    
    return resolved_links / total_links if total_links > 0 else 0

def main():
    print("🚀 Creating Laputa demo vault (v2 with pruning)\n")
    
    # Build graph
    nodes, link_lookup = build_graph()
    
    # Select notes
    selected = select_notes(nodes, link_lookup, target_count=1000)
    
    # Prune notes with too many dead links
    selected = prune_dead_link_notes(nodes, selected, link_lookup)
    
    # Check resolution
    link_resolution = verify_final_resolution(nodes, selected, link_lookup)
    
    print(f"\n✅ Final selection: {len(selected)} notes")
    print(f"   Link resolution: {link_resolution:.1%}")
    
    if link_resolution >= 0.80:
        # Copy files
        copied = copy_selected_notes(selected, nodes)
        
        # Final report
        print("\n" + "="*60)
        print("✅ DEMO VAULT CREATED")
        print("="*60)
        print(f"Total notes: {copied}")
        print(f"Link resolution: {link_resolution:.1%}")
        print(f"Location: {DEMO_ROOT}")
        
        return True
    else:
        print(f"\n⚠️  Link resolution {link_resolution:.1%} < 80% target")
        print("Copying anyway...")
        copied = copy_selected_notes(selected, nodes)
        print(f"Copied {copied} notes to {DEMO_ROOT}")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
