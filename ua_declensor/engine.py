from __future__ import annotations

from typing import Dict, Optional, Literal
import regex as re

from .utils import (
	apply_case_like,
	normalize_apostrophes,
	split_full_name,
	split_hyphenated,
	join_hyphenated,
)
from .rules import (
	CaseKey,
	Gender,
	Variant,
	SURNAME_RULES,
	GIVEN_RULES,
	PATR_RULES,
	find_rule,
)
from .names_loader import NamesConfig, load_names, detect_gender_by_given_name
from .exceptions_loader import ExceptionsConfig, load_exceptions


CASES_ORDER: list[CaseKey] = [
	"nominative",
	"genitive",
	"dative",
	"accusative",
	"instrumental",
	"locative",
	"vocative",
]

CASE_LABELS_UA: Dict[CaseKey, str] = {
	"nominative": "Називний",
	"genitive": "Родовий",
	"dative": "Давальний",
	"accusative": "Знахідний",
	"instrumental": "Орудний",
	"locative": "Місцевий",
	"vocative": "Кличний",
}


def _infer_gender(full_name: str, provided: Literal["m", "f", "auto"]) -> Optional[Gender]:
	if provided in ("m", "f"):
		return provided
	surname, given, _ = split_full_name(full_name)
	if given:
		names = load_names()
		return detect_gender_by_given_name(given, names)  # type: ignore[return-value]
	return None


def _apply_surname(surname: str, gender: Gender, case: CaseKey, variant: Variant, exc: ExceptionsConfig) -> str:
	# exceptions full override per case
	custom = exc.custom_forms.get(surname)
	if custom:
		gmap = custom.get(gender)
		if gmap:
			vmap = gmap.get("cases") or {}
			out = vmap.get(case)
			if out:
				return out
		# fallback for dative short/long if requested later
	# feminine invariable list for all cases except nominative
	if gender == "f" and surname in exc.invariable_feminine and case != "nominative":
		return surname
	# hyphenated
	parts = split_hyphenated(surname)
	declined: list[str] = []
	for idx, part in enumerate(parts):
		rule = find_rule(part, SURNAME_RULES, gender)
		if not rule:
			declined.append(part)
			continue
		# masculine hyphen heuristic for dative long on first, short on following
		per_variant = variant
		if gender == "m" and case == "dative" and variant == "long" and idx > 0:
			per_variant = "short"
		declined.append(rule.apply(part, case, per_variant))
	return join_hyphenated(declined)


def _apply_given(given: str, gender: Gender, case: CaseKey, variant: Variant) -> str:
	rule = find_rule(given, GIVEN_RULES, gender)
	return rule.apply(given, case, variant) if rule else given


def _apply_patronymic(patr: str, gender: Gender, case: CaseKey, variant: Variant) -> str:
	rule = find_rule(patr, PATR_RULES, gender)
	return rule.apply(patr, case, variant) if rule else patr


def decline_full_name_all_cases(
	full_name: str,
	gender: Literal["m", "f", "auto"] = "auto",
	surname_variant: Literal["short", "long"] = "long",
	keep_case: bool = True,
) -> Dict[CaseKey, str]:
	if not isinstance(full_name, str):
		raise TypeError("full_name must be a string")
	orig = full_name
	norm = normalize_apostrophes(orig).strip()

	maybe_gender = _infer_gender(norm, gender)
	if maybe_gender is None:
		# unknown: return nominative only
		surname, given, patr = split_full_name(norm)
		base = " ".join([p for p in [given, surname, patr] if p is not None])
		res = {c: base for c in CASES_ORDER}
		return {k: apply_case_like(orig, v, keep_case) for k, v in res.items()}

	exc = load_exceptions()
	surname, given, patr = split_full_name(norm)
	surname = surname or ""
	given = given or ""
	patr = patr or ""

	results: Dict[CaseKey, str] = {}
	for case in CASES_ORDER:
		decl_surname = _apply_surname(surname, maybe_gender, case, surname_variant, exc)
		decl_given = _apply_given(given, maybe_gender, case, surname_variant)
		decl_patr = _apply_patronymic(patr, maybe_gender, case, surname_variant)
		# Order as Given Surname Patronymic per example
		joined = " ".join([w for w in [decl_given, decl_surname, decl_patr] if w])
		results[case] = apply_case_like(orig, joined, keep_case)
	return results