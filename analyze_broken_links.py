#!/usr/bin/env python3
"""Analyze which broken links are to existing vs non-existent notes."""

import sys
sys.path.insert(0, '/Users/luca/Workspace/laputa-app')
from select_demo_notes import build_graph, select_notes, LAPUTA_ROOT

nodes, link_lookup = build_graph()
selected = select_notes(nodes, link_lookup, target_count=1000)

print("\n🔍 Analyzing broken links...")

# Count links by type
total_outlinks = 0
resolved = 0
unresolved_but_exists = 0
unresolved_not_exists = 0

for path in selected:
    node = nodes[path]
    for link_ref in node['outlinks']:
        total_outlinks += 1
        
        if link_ref in link_lookup:
            target = link_lookup[link_ref]
            if target in selected:
                resolved += 1
            else:
                # Exists but not in selection
                unresolved_but_exists += 1
        else:
            # Doesn't exist at all
            unresolved_not_exists += 1

print(f"Total outlinks: {total_outlinks}")
print(f"  Resolved (in selection): {resolved} ({resolved/total_outlinks*100:.1f}%)")
print(f"  Unresolved but note exists: {unresolved_but_exists} ({unresolved_but_exists/total_outlinks*100:.1f}%)")
print(f"  Unresolved - note doesn't exist: {unresolved_not_exists} ({unresolved_not_exists/total_outlinks*100:.1f}%)")

print(f"\nIf we include ALL existing notes (not just selected):")
print(f"  Max possible resolution: {(resolved + unresolved_but_exists)/total_outlinks*100:.1f}%")
