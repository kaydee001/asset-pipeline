import os
from typing import List

ROOT_DIR = r"D:\Users\kartik\Desktop\pipeline-projects\asset-pipeline"
ALLOWED_EXTENSIONS = ['.fbx', '.blend']


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
        if " " in file_name or any(c.isupper() for c in os.path.basename(file_name)):
            err_name.append(file_name+file_ext)
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


if __name__ == "__main__":
    scanned_assets = scan_assets(ROOT_DIR, ALLOWED_EXTENSIONS)
    asset_count = count_assets(scanned_assets)
    check_name = name_checker(scanned_assets)

    generate_report(scanned_assets, asset_count, check_name)
