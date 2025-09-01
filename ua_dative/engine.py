from __future__ import annotations

from typing import Literal, Optional
import regex as re
import pandas as pd  # used in CLI but safe import

from .utils import (
	Gender,
	Variant,
	apply_case_like,
	normalize_apostrophes,
	split_full_name,
	split_hyphenated,
	join_hyphenated,
)
from .rules import find_rule
from .exceptions_loader import ExceptionsConfig, load_exceptions
from .names_loader import NamesConfig, load_names, detect_gender_by_given_name


DEFAULT_VARIANT: Variant = "long"


def _infer_gender(full_name: str, provided: Literal["m", "f", "auto"]) -> Optional[Gender]:
	if provided in ("m", "f"):
		return provided
	surname, given, _ = split_full_name(full_name)
	if given:
		names = load_names()
		return detect_gender_by_given_name(given, names)
	return None


def _extract_surname(full_name: str) -> str:
	surname, given, patronymic = split_full_name(full_name)
	return surname


def _apply_rule(surname: str, gender: Gender, variant: Variant, exc: ExceptionsConfig) -> str:
	# Exceptions override
	custom = exc.custom_forms.get(surname)
	if custom:
		gmap = custom.get(gender)
		if gmap:
			if variant == "short":
				return gmap.get("short") or gmap.get("long") or surname
			if variant == "long" or variant == "auto":
				return gmap.get("long") or gmap.get("short") or surname
	# Invariable feminine list
	if gender == "f" and surname in exc.invariable_feminine:
		return surname

	rule = find_rule(surname, gender)
	if not rule:
		return surname
	use_variant: Variant = DEFAULT_VARIANT if variant == "auto" else variant
	return rule.apply(surname, use_variant)


def to_dative(
	surname: str,
	gender: Literal["m", "f", "auto"] = "auto",
	variant: Variant = "auto",
	keep_case: bool = True,
) -> str:
	"""Convert a surname or full name to dative case, preserving original casing.

	- Accepts hyphenated surnames by declining each part.
	- Auto-detect gender from given name if available.
	- Exceptions override rules.
	"""
	if not isinstance(surname, str):
		raise TypeError("surname must be a string")

	original = surname
	norm = normalize_apostrophes(original).strip()

	# Determine gender
	maybe_gender = _infer_gender(norm, gender)
	if maybe_gender is None:
		# Ambiguous: no gender; return unchanged to allow Excel to warn via separate UDF
		return apply_case_like(original, _extract_surname(norm), keep_case)

	exc = load_exceptions()

	# Work on hyphenated surname only
	surname_only = _extract_surname(norm)
	parts = split_hyphenated(surname_only)

	# Decide base variant
	overall_variant: Variant = DEFAULT_VARIANT if variant == "auto" else variant
	declined_parts: list[str] = []
	for idx, p in enumerate(parts):
		per_variant: Variant = overall_variant
		# Heuristic: for masculine hyphenated surnames with long variant, prefer short for subsequent parts
		if maybe_gender == "m" and overall_variant == "long" and idx > 0:
			per_variant = "short"
		declined_parts.append(_apply_rule(p, maybe_gender, per_variant, exc))

	result = join_hyphenated(declined_parts)

	return apply_case_like(original, result, keep_case)