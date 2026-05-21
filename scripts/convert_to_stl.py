import sys
import os
import glob

sys.path.append('/Applications/FreeCAD.app/Contents/Resources/lib')

import FreeCAD
import Mesh

input_dir = os.path.dirname(os.path.abspath(__file__))
fcstd_files = glob.glob(os.path.join(input_dir, '*.FCStd'))

print(f"Found {len(fcstd_files)} FCStd files")

for fcstd_path in fcstd_files:
    basename = os.path.splitext(os.path.basename(fcstd_path))[0]
    stl_path = os.path.join(input_dir, basename + '.stl')
    print(f"Converting: {basename}.FCStd -> {basename}.stl")

    try:
        doc = FreeCAD.open(fcstd_path)
        shapes = []

        for obj in doc.Objects:
            if hasattr(obj, 'Shape') and obj.Shape and not obj.Shape.isNull():
                shapes.append(obj)

        if not shapes:
            print(f"  WARNING: No shapes found in {basename}")
            FreeCAD.closeDocument(doc.Name)
            continue

        mesh_parts = []
        for obj in shapes:
            mesh = Mesh.Mesh()
            Mesh.export([obj], '/tmp/_tmp_mesh.stl')
            mesh_parts.append('/tmp/_tmp_mesh.stl')

        # Export all shapes together
        Mesh.export(shapes, stl_path)
        print(f"  OK: {stl_path}")
        FreeCAD.closeDocument(doc.Name)

    except Exception as e:
        print(f"  ERROR: {e}")

print("Done.")
