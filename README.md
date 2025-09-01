# UA Dative Surnames & UA Declensor

Tools for declining Ukrainian surnames and full names. Works offline.

## UA Declensor (GUI)

Run locally (development):

```bash
python -m pip install -e .[dev]
python -m ua_declensor.gui
```

Pack to Windows .exe (from Windows):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole ua_declensor.py
# Dist output: dist/ua_declensor.exe  → rename to UA_Declensor.exe
```

Usage in app:
- Paste full name: "Петренко Іван Іванович"
- Choose Gender: auto/m/f (auto by default)
- Click Decline → table shows 7 cases
- Export to Excel → saves cases.xlsx

## UA Dative (Excel/CLI)

Excel UDF:
```excel
=UA_DATIVE(A2, "m", "long", TRUE)
```

CLI:
```bash
python -m ua_dative.cli --input in.xlsx --sheet Sheet1 \
  --col Surname --gender-col Gender --output out.xlsx \
  --out-col Dative --variant long --keep-case true --report
```

## Exceptions and Names

- Edit `ua_dative/exceptions.yml` or `ua_declensor/exceptions.yml` to add overrides or invariable forms.
- Edit `ua_dative/names.yml` or `ua_declensor/names.yml` to add male/female given names for auto-detection.