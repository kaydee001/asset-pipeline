import os
import subprocess
from scanner import scan_assets

blend_files = scan_assets(
    r"D:\Users\kartik\Desktop\pipeline-projects\asset-pipeline", [".blend"])

for file in blend_files:
    # print(os.path.basename(file))
    subprocess.run(["blender", "-b", file,
                    "-P", "scene_validator.py"])
