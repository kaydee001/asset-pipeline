import bpy
import os
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--output", help="output folder for json",  default=r"D:\Users\kartik\Desktop\pipeline-projects\asset-pipeline\exports")
parser.add_argument("--poly-limit", type=int, default=200)

args, _ = parser.parse_known_args()


def scene_validator(obj):
    warnings = []
    name = obj.name
    count = len(obj.data.polygons)
    if count > args.poly_limit:
        warnings.append(f"HIGH POLY : {obj.name} has {count} polygons")
    if any(ch.isupper() for ch in name):
        warnings.append(f"BAD NAME : {name}")
    return warnings


def rename_objs(mesh_obj):
    cleaned_name = mesh_obj.name.replace(" ", "").lower()
    return cleaned_name


def create_json_report(warnings):
    os.makedirs(args.output, exist_ok=True)

    data = {"file": os.path.basename(bpy.data.filepath),
            "total_warnings": len(warnings),
            "warnings": warnings
            }
    json_path = os.path.join(args.output, "export_data.json")

    with open(json_path, 'w') as file:
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


def run_pipeline():
    warnings_list = []
    for obj in bpy.data.objects:
        if obj.type == "MESH":
            warnings_list += scene_validator(obj)

    for obj in bpy.data.objects:
        if obj.type == "MESH":
            new_name = rename_objs(obj)
            obj.name = new_name

    create_json_report(warnings_list)
    batch_export(args.output)


run_pipeline()
