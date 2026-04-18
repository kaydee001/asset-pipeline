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

## Roadmap
- [ ] Auto-fix naming issues
- [ ] Blender export integration
- [ ] GUI wrapper```
