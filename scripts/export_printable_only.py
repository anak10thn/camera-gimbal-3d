import sys
sys.path.append('/Applications/FreeCAD.app/Contents/Resources/lib')
import FreeCAD
import Mesh

BASE = '/Users/anak10thn/Documents/ROBOT-3D/camera+gimbal/'
OUT  = BASE + '3d printer/'

# { file: [ (object_label, output_stl_name) ] }
EXPORT_MAP = {
    'Kamera_Basis.FCStd': [
        ('Deckel',   'Kamera_Basis_Deckel.stl'),
        ('Gehäuse',  'Kamera_Basis_Gehaeuse.stl'),
    ],
    'Achsverbindung.FCStd': [
        ('Verbinder', 'Achsverbindung.stl'),
    ],
    'Kamera_Halterung.FCStd': [
        ('Kamerahalterung', 'Kamera_Halterung.stl'),
    ],
}

for fname, targets in EXPORT_MAP.items():
    print(f"\n--- {fname} ---")
    doc = FreeCAD.open(BASE + fname)

    label_map = {obj.Label: obj for obj in doc.Objects}

    for label, stl_name in targets:
        if label not in label_map:
            print(f"  NOT FOUND: {label}")
            continue
        obj = label_map[label]
        out_path = OUT + stl_name
        try:
            Mesh.export([obj], out_path)
            print(f"  OK: {stl_name}")
        except Exception as e:
            print(f"  ERROR {label}: {e}")

    FreeCAD.closeDocument(doc.Name)

print("\nDone.")
