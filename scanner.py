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


def find_duplicates(assets):
    total_assets = {}
    for asset in assets:
        file_name, file_ext = os.path.splitext(asset)
        asset_name = os.path.basename(file_name) + file_ext
        at = total_assets.setdefault(asset_name, [])
        at.append(asset)
    duplicate_assets = {k: v for k,
                        v in total_assets.items() if len(v) > 1}
    return duplicate_assets


def generate_report(scanned_assets, asset_count, check_name, duplicate_assets):
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
        print("duplicated assets found", file=file)
        if len(duplicate_assets) < 1:
            print(" : none", file=file)
        else:
            for asset_name, asset_path in duplicate_assets.items():
                print(f" - {asset_name} : {asset_path}", file=file)

        file.write("="*20)


def export_json_report(scaned_assets, asset_count, check_name, duplicate_assets):
    data = {"total_assets": len(
        scaned_assets),
        "asset_count": asset_count,
        "naming_issues": check_name,
        "duplicated_assets": duplicate_assets}

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    scanned_assets = scan_assets(ROOT_DIR, ALLOWED_EXTENSIONS)
    asset_count = count_assets(scanned_assets)
    check_name = name_checker(scanned_assets)
    dup_assets = find_duplicates(scanned_assets)

    generate_report(scanned_assets, asset_count, check_name, dup_assets)
    export_json_report(scanned_assets, asset_count, check_name, dup_assets)
    # for asset_name, asset_path in dup_assets.items():
    #     print(f"{asset_name} : {asset_path}")
