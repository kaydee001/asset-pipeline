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
        if " " in file_name:
            err_name.append(file_name+file_ext)
    return err_name


if __name__ == "__main__":
    scanned_assets = scan_assets(ROOT_DIR, ALLOWED_EXTENSIONS)

    print(f"Asset Pipeline Report")
    print("="*20)
    asset_count = count_assets(scanned_assets)
    print(f"total assets found {len(scanned_assets)} : ")

    for key, value in asset_count.items():
        print(f" -{key} : ", value)

    check_name = name_checker(scanned_assets)
    print(f"naming issues : {len(check_name)}")
    for asset in check_name:
        print(
            f" - {os.path.basename(asset)}")
    print("="*20)
