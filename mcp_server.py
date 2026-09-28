import sys
import json
from client import BVHRayTracer

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "ray_aabb_intersect",
                        "description": "Perform fast slab method ray-AABB intersection test",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "ray_origin": {"type": "array", "items": {"type": "number"}},
                                "ray_direction": {"type": "array", "items": {"type": "number"}},
                                "aabb_min": {"type": "array", "items": {"type": "number"}},
                                "aabb_max": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["ray_origin", "ray_direction", "aabb_min", "aabb_max"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "ray_aabb_intersect":
            hit, t = BVHRayTracer.intersect_ray_aabb(
                args["ray_origin"], args["ray_direction"], args["aabb_min"], args["aabb_max"]
            )
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"hit": hit, "distance": t})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
