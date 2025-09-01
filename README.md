# UA Dative Surnames

Offline tool to decline Ukrainian surnames into the dative case with Excel integration.

## Installation

Use a clean folder or a virtual environment. In this repo layout, install editable:

```bash
pip install -e .[dev]
```

## Usage

- Excel (xlwings UDF):
```excel
=UA_DATIVE(A2, "m", "long", TRUE)
```

- CLI:
```bash
python -m ua_dative.cli --input in.xlsx --sheet Sheet1 \
  --col Surname --gender-col Gender --output out.xlsx \
  --out-col Dative --variant long --keep-case true
```

See `ua_dative/exceptions.yml` and `ua_dative/names.yml` for configuration of exceptions and name-gender detection.