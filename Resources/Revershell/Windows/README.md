# Windows Reverse Shell

## Ofuscación

```bash
pyarmor gen rs.py
```

## Compilación

```bash
pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/xabie/Pictures/PFP/pfp.ico" --hide-console "hide-early" --add-data "C:/Users/xabie/Documents/GitHub/htb/Resources/Revershell/Windows/dist/pyarmor_runtime_000000;pyarmor_runtime_000000/"  "C:/Users/xabie/Documents/GitHub/htb/Resources/Revershell/Windows/dist/rs.py"
```
