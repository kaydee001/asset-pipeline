import bpy
import os
import json

output_path = r"D:\Users\kartik\Desktop\pipeline-projects\asset-pipeline\exports"


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


def batch_export(output_path):
    os.makedirs(output_path, exist_ok=True)
    export_type = ".fbx"

    for obj in bpy.data.objects:
        if obj.type == "MESH":
            bpy.ops.object.select_all(action="DESELECT")
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj

            obj_path = os.path.join(output_path, obj.name+export_type)

            bpy.ops.export_scene.fbx(filepath=obj_path, use_selection=True)


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
batch_export(output_path)
