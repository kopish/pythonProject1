from __future__ import annotations

import argparse
from typing import Optional
import pandas as pd

from .engine import to_dative
from .names_loader import load_names, detect_gender_by_given_name
from .utils import split_full_name


def process_dataframe(
	df: pd.DataFrame,
	surname_col: str,
	gender_col: Optional[str],
	out_col: str,
	variant: str,
	keep_case: bool,
	report: bool = False,
) -> tuple[pd.DataFrame, dict[str, int]]:
	report_stats = {
		"auto_gender_total": 0,
		"auto_gender_ambiguous": 0,
		"exceptions_used": 0,  # reserved for future detailed tracking
	}

	names = load_names()

	def row_to_gender(name: str, gval: Optional[str]) -> str:
		if gval in ("m", "f"):
			return gval
		_, given, _ = split_full_name(name)
		if given:
			report_stats["auto_gender_total"] += 1
			g_auto = detect_gender_by_given_name(given, names)
			if g_auto is None:
				report_stats["auto_gender_ambiguous"] += 1
				return "auto"
			return g_auto  # type: ignore[return-value]
		return "auto"

	out_vals: list[str] = []
	for _, row in df.iterrows():
		name = str(row[surname_col])
		gparam = str(row[gender_col]) if gender_col and gender_col in row and pd.notna(row[gender_col]) else None
		gender = row_to_gender(name, gparam)
		out_vals.append(to_dative(name, gender, variant, keep_case))

	df[out_col] = out_vals
	return df, report_stats


def main(argv: Optional[list[str]] = None) -> None:
	parser = argparse.ArgumentParser(description="UA Dative Surnames batch tool")
	parser.add_argument("--input", required=True)
	parser.add_argument("--sheet", required=False)
	parser.add_argument("--col", dest="surname_col", required=True)
	parser.add_argument("--gender-col", dest="gender_col")
	parser.add_argument("--output", required=True)
	parser.add_argument("--out-col", dest="out_col", required=True)
	parser.add_argument("--variant", choices=["auto", "short", "long"], default="auto")
	parser.add_argument("--keep-case", dest="keep_case", choices=["true", "false"], default="true")
	parser.add_argument("--report", action="store_true")
	args = parser.parse_args(argv)

	keep_case = args.keep_case.lower() == "true"

	# Read workbook
	if args.sheet:
		df = pd.read_excel(args.input, sheet_name=args.sheet, engine="openpyxl")
	else:
		df = pd.read_excel(args.input, engine="openpyxl")

	processed, stats = process_dataframe(
		df=df,
		surname_col=args.surname_col,
		gender_col=args.gender_col,
		out_col=args.out_col,
		variant=args.variant,
		keep_case=keep_case,
		report=args.report,
	)

	# Write back preserving other columns
	with pd.ExcelWriter(args.output, engine="openpyxl", mode="w") as writer:
		processed.to_excel(writer, index=False, sheet_name=(args.sheet or "Sheet1"))

	if args.report:
		print("Report:")
		for k, v in stats.items():
			print(f"{k}: {v}")


if __name__ == "__main__":  # pragma: no cover
	main()