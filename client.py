"""BVH Ray-AABB Intersection Engine.
100% Python Standard Library.
"""

class BVHRayTracer:
    """Fast slab method ray-AABB intersection tester."""
    @staticmethod
    def intersect_ray_aabb(ray_orig, ray_dir, aabb_min, aabb_max):
        tmin = -float("inf")
        tmax = float("inf")
        for i in range(len(ray_orig)):
            if ray_dir[i] != 0:
                t1 = (aabb_min[i] - ray_orig[i]) / ray_dir[i]
                t2 = (aabb_max[i] - ray_orig[i]) / ray_dir[i]
                tmin = max(tmin, min(t1, t2))
                tmax = min(tmax, max(t1, t2))
            else:
                if ray_orig[i] < aabb_min[i] or ray_orig[i] > aabb_max[i]:
                    return False, 0.0
        return (tmax >= max(0.0, tmin)), max(0.0, tmin)
