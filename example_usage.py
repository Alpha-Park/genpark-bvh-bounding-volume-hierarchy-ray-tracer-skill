from client import BVHRayTracer

hit, dist = BVHRayTracer.intersect_ray_aabb(
    ray_orig=(0, 0, -10),
    ray_dir=(0, 0, 1),
    aabb_min=(-2, -2, 0),
    aabb_max=(2, 2, 5)
)
print(f"Ray Hit Box: {hit} at distance: {dist}")
