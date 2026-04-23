# Asset Pipeline Tool

A Python-based CLI tool to scan, validate, and report on 3D asset folders before handoff.

## Features
- Recursive folder scanning for 3D assets
- Filter by file extension (.fbx, .blend, .obj, etc.)
- Naming convention checker (flags spaces and uppercase)
- Duplicate file detector
- Generates TXT and JSON reports
- Configurable via `config.json` or CLI arguments

## Usage

### Using config file
Edit `config.json` with your folder path and extensions, then run:
```
python scanner.py
```

### Using CLI arguments
```
python scanner.py --folder "D:/my_assets" --ext .fbx .blend
```

## Config
```json
{
    "root_dir": "path/to/your/assets",
    "allowed_extensions": [".fbx", ".blend"]
}
```

## Output
- `report.txt` — human readable summary
- `data.json` — machine readable report

## Scripts

### scanner.py
Scans a folder for 3D assets. Filters by extension, detects naming issues and duplicates. Outputs TXT and JSON reports.

### scene_validator.py  
Runs inside Blender to validate a scene. Checks poly limits, naming conventions. Batch renames objects and exports FBX files.

### run_pipeline.py
Master script. Finds all .blend files in a folder and runs scene_validator.py on each one automatically using subprocess.

## CLI Usage

**scanner.py**
python scanner.py --folder "path/to/assets" --ext .fbx .blend --fix

**scene_validator.py**
blender -b scene.blend -P scene_validator.py

**run_pipeline.py**
python run_pipeline.py