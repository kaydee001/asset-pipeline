import os
from typing import List

root_dir = r"D:\Users\kartik\Desktop\pipeline-projects\asset-pipeline"
ALLOWED_EXTENSIONS = ['.fbx', '.blend']

# for file in os.listdir(root_dir):
#     if os.path.isfile(file):
#         file_name, file_ext = os.path.splitext(file)
#         path = os.path.join(root_dir, file)
#         print("path : ", path)

# for root, dirs, files in os.walk(root_dir):
#     for file in files:

#         path = os.path.join(root, file)
#         _, file_ext = os.path.splitext(file)

#         if file_ext in ALLOWED_EXTENSIONS:
#             print("files : ", path)


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


# for asset in scanned_assets:
#     print(asset)

# print(f"found {len(scanned_assets)} assets : ")

# for key, value in asset_count.items():
#     print(f" -{key} : ", value)


if __name__ == "__main__":
    scanned_assets = scan_assets(root_dir, ALLOWED_EXTENSIONS)

    asset_count = count_assets(scanned_assets)

    check_name = name_checker(scanned_assets)
    for asset in check_name:
        print(
            f"warning : {os.path.basename(asset)} contains space in filename")
