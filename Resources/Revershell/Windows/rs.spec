# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/xabie/Documents/GitHub/htb/Resources/Revershell/Windows/dist/rs.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/xabie/Documents/GitHub/htb/Resources/Revershell/Windows/dist/pyarmor_runtime_000000', 'pyarmor_runtime_000000/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='rs',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\xabie\\Pictures\\PFP\\pfp.ico'],
    hide_console='hide-early',
)
