import os
import json
from typing import List

# ROOT_DIR = r"D:\Users\kartik\Desktop\pipeline-projects\asset-pipeline"
# ALLOWED_EXTENSIONS = ['.fbx', '.blend']

try:
    with open('config.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("config not found")
    exit(1)
except json.JSONDecodeError:
    print("not a valid json file")
    exit(1)

ROOT_DIR = data["root_dir"]
ALLOWED_EXTENSIONS = data["allowed_extensions"]


def scan_assets(folder, extensions) -> List:
    assets = []

    for root, dirs, files in os.walk(folder):
        for file in files:

            path = os.path.join(root, file)
            _, file_ext = os.path.splitext(file)

            if file_ext in extensions:
                assets.append(path)

    return assets


def count_assets(assets):
    asset_count = {}
    for asset in assets:
        _, file_ext = os.path.splitext(asset)
        asset_count[file_ext] = asset_count.get(file_ext, 0) + 1
    return asset_count


def name_checker(assets):
    err_name = []
    for asset in assets:
        file_name, file_ext = os.path.splitext(asset)
        if " " in os.path.basename(file_name) or any(c.isupper() for c in os.path.basename(file_name)):
            err_name.append(os.path.basename(file_name)+file_ext)
    return err_name


def generate_report(scanned_assets, asset_count, check_name):
    with open("report.txt", "w") as file:
        print(f"Asset Pipeline Report", file=file)
        print("="*20, file=file)
        print(f"total assets found {len(scanned_assets)} : ", file=file)
        for key, value in asset_count.items():
            print(f"-{key} : {value}", file=file)
        print(f"naming issues : {len(check_name)}", file=file)
        for asset in check_name:
            print(
                f"- {os.path.basename(asset)}", file=file)
        file.write("="*20)


def export_json_report(scaned_assets, asset_count, check_name):
    data = {"total_assets": len(
        scaned_assets),
        "asset_count": asset_count,
        "naming_issues": check_name}

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    scanned_assets = scan_assets(ROOT_DIR, ALLOWED_EXTENSIONS)
    asset_count = count_assets(scanned_assets)
    check_name = name_checker(scanned_assets)

    generate_report(scanned_assets, asset_count, check_name)
    export_json_report(scanned_assets, asset_count, check_name)
