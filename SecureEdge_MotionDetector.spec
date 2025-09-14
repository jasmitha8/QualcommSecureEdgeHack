# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\motion_detector.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/qc_de/Desktop/SecureEdge/venv/Lib/site-packages/ultralytics', 'ultralytics')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['polars', 'transformers'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SecureEdge_MotionDetector',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
