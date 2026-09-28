# BVH Ray-AABB Intersection Skill

High-efficiency, zero-dependency Python implementation of **BVH Ray-AABB Slab Intersection** for real-time ray tracing and rendering acceleration.

## Features
- **Slab Method Intersection**: Computes coordinate interval overlaps across 3D planes without trigonometric functions.
- **Fast Hit Distance**: Evaluates closest entry distance \(t_{\min}\) for sorting ray traversal stacks.
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph LR
    Ray["Ray (Origin + t*Dir)"] --> SlabX["X-Axis Slab [t_1x, t_2x]"]
    Ray --> SlabY["Y-Axis Slab [t_1y, t_2y]"]
    Ray --> SlabZ["Z-Axis Slab [t_1z, t_2z]"]
    SlabX & SlabY & SlabZ --> IntervalOverlap["t_enter <= t_exit and t_exit >= 0"]
    IntervalOverlap --> Hit["Ray Hits Bounding Box"]
```
