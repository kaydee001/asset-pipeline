import bpy
import os
import json


def scene_validator(obj):
    warnings = []
    name = obj.name
    count = len(obj.data.polygons)
    if count > 200:
        warnings.append(f"HIGH POLY : {obj.name} has {count} polygons")
    if any(ch.isupper() for ch in name):
        warnings.append(f"BAD NAME : {name}")
    return warnings


def rename_objs(mesh_obj):
    renamed_obj = mesh_obj.name.replace(" ", "").lower()
    return renamed_obj


def create_json_report(warnings):
    data = {"file": os.path.basename(bpy.data.filepath),
            "total_warnings": len(warnings),
            "warnings": warnings
            }

    with open('export_data.json', 'w') as file:
        json.dump(data, file, indent=4)


warnings_list = []
for obj in bpy.data.objects:
    if obj.type == "MESH":
        warnings_list += scene_validator(obj)

for obj in bpy.data.objects:
    if obj.type == "MESH":
        new_name = rename_objs(obj)
        obj.name = new_name

# for warning in warnings_list:
#     print(warning)

create_json_report(warnings_list)
