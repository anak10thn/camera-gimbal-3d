# Camera Gimbal 3D

A 3D-printable camera gimbal designed in FreeCAD. Supports standard **webcam** mounting with servo-driven pan/tilt motion.

## Repository Structure

```
.
├── stl/          # Print-ready STL files (servo & screws removed)
├── freecad/      # FreeCAD source files (.FCStd)
└── scripts/      # FCStd → STL conversion scripts
```

## Printable Parts (`stl/`)

| File | Description |
|------|-------------|
| `Kamera_Basis_Deckel.stl` | Camera base lid / top cover |
| `Kamera_Basis_Gehaeuse.stl` | Camera base housing |
| `Kamera_Halterung.stl` | Camera bracket / holder |
| `Achsverbindung.stl` | Gimbal axis connector |
| `Befestigung.stl` | Mounting bracket |
| `T25_servo_horn.stl` | Custom T25 servo horn |

> STL files are exported clean — servo bodies and screws are excluded. Only the parts you need to print.

## Camera Compatibility

This gimbal is designed to mount a standard **USB webcam**. The `Kamera_Halterung` (camera holder) fits common rectangular webcam form factors. Reference model: `freecad/Webcam.FCStd`.

## FreeCAD Source (`freecad/`)

| File | Description |
|------|-------------|
| `Kamera.FCStd` | Full gimbal assembly |
| `Kamera_Basis.FCStd` | Camera base (lid + housing) |
| `Kamera_Halterung.FCStd` | Camera holder |
| `Achsverbindung.FCStd` | Axis connector |
| `Befestigung.FCStd` | Mounting bracket |
| `T25_servo_horn.FCStd` | T25 servo horn |
| `Webcam.FCStd` | Webcam reference model (not printed) |

## Scripts (`scripts/`)

| Script | Purpose |
|--------|---------|
| `export_printable_only.py` | Export only printable bodies from each assembly (excludes servo, screws) |
| `convert_to_stl.py` | Batch convert all FCStd files to STL |

### Usage

Requires FreeCAD (macOS: `brew install --cask freecad`).

```bash
# Export clean printable parts from the Kamera assembly
/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd scripts/export_printable_only.py

# Batch convert all FCStd to STL
/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd scripts/convert_to_stl.py
```

## Additional Hardware (Not Printed)

| Item | Notes |
|------|-------|
| Servo motor | T25 horn compatible |
| USB webcam | Mounted in `Kamera_Halterung` |
| M3 × 5 screws | Axis connector |
| M4 × 12 screws + M4 nuts | Base and holder |
| M1.6 × 8 screws | Camera attachment |

## Requirements

- [FreeCAD](https://www.freecad.org/) 1.1+
