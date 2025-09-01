from __future__ import annotations

import argparse

from .engine import decline_full_name_all_cases, CASES_ORDER, CASE_LABELS_UA


def main(argv: list[str] | None = None) -> None:
	parser = argparse.ArgumentParser(description="UA Declensor CLI")
	parser.add_argument("full_name")
	parser.add_argument("--gender", choices=["auto", "m", "f"], default="auto")
	args = parser.parse_args(argv)

	res = decline_full_name_all_cases(args.full_name, gender=args.gender)  # type: ignore[arg-type]
	for c in CASES_ORDER:
		print(f"{CASE_LABELS_UA[c]}:\t{res[c]}")


if __name__ == "__main__":  # pragma: no cover
	main()