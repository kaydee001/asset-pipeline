import bpy


def scene_validator(obj):
    warnings = []
    name = obj.name
    count = len(obj.data.polygons)
    if count > 200:
        warnings.append(f"HIGH POLY : {obj.name} has {count} polygons")
    if any(ch.isupper() for ch in name):
        warnings.append(f"BAD NAME : {name}")
    return warnings


warnings_list = []
for obj in bpy.data.objects:
    if obj.type == "MESH":
        warnings_list += scene_validator(obj)

for warning in warnings_list:
    print(warning)
