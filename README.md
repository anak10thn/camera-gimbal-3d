# Camera Gimbal 3D

Desain 3D untuk camera gimbal — FreeCAD source files dan STL siap cetak.

## Struktur

```
.
├── stl/                    # File STL siap cetak
├── freecad/                # Source file FreeCAD (.FCStd)
└── scripts/                # Script konversi FCStd → STL
```

## Komponen yang Dapat Dicetak (`stl/`)

| File | Deskripsi |
|------|-----------|
| `Kamera_Basis_Deckel.stl` | Tutup/cover dudukan kamera |
| `Kamera_Basis_Gehaeuse.stl` | Housing dudukan kamera |
| `Kamera_Halterung.stl` | Bracket holder kamera |
| `Achsverbindung.stl` | Penghubung sumbu gimbal |
| `Befestigung.stl` | Bracket pemasangan |
| `T25_servo_horn.stl` | Servo horn kustom T25 |

> **Catatan:** STL sudah dibersihkan dari komponen servo dan baut — hanya bagian yang perlu dicetak.

## FreeCAD Source (`freecad/`)

| File | Deskripsi |
|------|-----------|
| `Kamera.FCStd` | Assembly lengkap kamera gimbal |
| `Kamera_Basis.FCStd` | Dudukan kamera (Deckel + Gehäuse) |
| `Kamera_Halterung.FCStd` | Holder kamera |
| `Achsverbindung.FCStd` | Penghubung sumbu |
| `Befestigung.FCStd` | Bracket pemasangan |
| `T25_servo_horn.FCStd` | Servo horn T25 |
| `Webcam.FCStd` | Model referensi webcam (tidak dicetak) |

## Scripts (`scripts/`)

| Script | Fungsi |
|--------|--------|
| `export_printable_only.py` | Export hanya body yang dapat dicetak per komponen (tanpa servo, baut) |
| `convert_to_stl.py` | Konversi batch semua FCStd ke STL |

### Cara Pakai Script

Membutuhkan FreeCAD terinstall (via Homebrew: `brew install --cask freecad`).

```bash
# Export komponen printable dari assembly Kamera.FCStd
/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd scripts/export_printable_only.py

# Konversi semua FCStd ke STL sekaligus
/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd scripts/convert_to_stl.py
```

## Hardware Tambahan (Tidak Dicetak)

- Servo motor (kompatibel T25 horn)
- Webcam / kamera
- Baut M3, M4
- Baut M1.6x8 (untuk kamera)

## Tools

- [FreeCAD](https://www.freecad.org/) 1.1+
