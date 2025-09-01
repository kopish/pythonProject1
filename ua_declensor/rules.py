from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal, Optional
import regex as re

from .utils import split_hyphenated, join_hyphenated

Gender = Literal["m", "f"]
Variant = Literal["short", "long"]
CaseKey = Literal[
	"nominative", "genitive", "dative", "accusative", "instrumental", "locative", "vocative",
]


@dataclass(frozen=True)
class Rule:
	name: str
	target: Literal["given", "surname", "patronymic"]
	gender: Optional[Gender]
	pattern: re.Pattern[str]
	priority: int
	apply: Callable[[str, CaseKey, Variant], str]


def _re(s: str) -> re.Pattern[str]:
	return re.compile(s, re.IGNORECASE)


# --- Helper apply functions (surnames) ---

def _m_surname_hard(full: str, case: CaseKey, variant: Variant) -> str:
	if case == "genitive" or case == "accusative":
		return full + "а"
	if case == "dative":
		return (full + "ові") if variant == "long" else (full + "у")
	if case == "instrumental":
		return full + "ом"
	if case == "locative":
		return full + "і"
	if case == "vocative":
		return full + "е"
	return full


def _m_surname_soft(full: str, case: CaseKey, variant: Variant) -> str:
	# ex: Коваль, Гайдай
	if full.endswith("й"):
		stem = full[:-1]
		if case in ("genitive", "accusative"):
			return stem + "я"
		if case == "dative":
			# -ай -> -аєві (write as stem + 'єві'), else -еві
			return (stem + ("єві" if full.endswith("ай") else "еві")) if variant == "long" else (stem + "ю")
		if case == "instrumental":
			return stem + "єм"
		if case == "locative":
			return stem + ("єві" if full.endswith("ай") else "еві")
		if case == "vocative":
			return stem + "ю"
		return full
	# soft sign (ль, нь)
	stem = full[:-1]
	if case in ("genitive", "accusative"):
		return stem + "я"
	if case == "dative":
		return (stem + "еві") if variant == "long" else (stem + "ю")
	if case == "instrumental":
		return stem + "ем"
	if case == "locative":
		return stem + "еві"
	if case == "vocative":
		return stem + "ю"
	return full


def _m_surname_enko_ko(full: str, case: CaseKey, variant: Variant) -> str:
	stem = full[:-1]
	if case in ("genitive", "accusative"):
		return stem + "а"
	if case == "dative":
		return (stem + "ові") if variant == "long" else (stem + "у")
	if case == "instrumental":
		return stem + "ом"
	if case == "locative":
		return stem + "ові"
	if case == "vocative":
		return stem + "о"
	return full


def _m_surname_adj_iy(full: str, case: CaseKey, variant: Variant) -> str:
	base = full[:-2]
	if case == "genitive" or case == "accusative":
		return base + "ого"
	if case == "dative":
		return base + "ому"
	if case == "instrumental":
		return base + "им"
	if case == "locative":
		return base + "ому"
	if case == "vocative":
		return base + "ий"
	return full


def _m_surname_ch_shch(full: str, case: CaseKey, variant: Variant) -> str:
	if case in ("genitive", "accusative"):
		return full + "а"
	if case == "dative":
		return (full + "еві") if variant == "long" else (full + "у")
	if case == "instrumental":
		return full + "ем"
	if case == "locative":
		return full + "еві"
	if case == "vocative":
		return full + "у"
	return full


def _m_surname_etz(full: str, case: CaseKey, variant: Variant) -> str:
	stem = full[:-3]
	if case in ("genitive", "accusative"):
		return stem + "ця"
	if case == "dative":
		return (stem + "цеві") if variant == "long" else (stem + "цю")
	if case == "instrumental":
		return stem + "цем"
	if case == "locative":
		return stem + "цеві"
	if case == "vocative":
		return stem + "цю"
	return full

# Feminine surname rules

def _f_surname_special_slavic(full: str, case: CaseKey, variant: Variant) -> str:
	m = re.search(r"(?i)(.+)(ова|єва|ева|іна|їна)$", full)
	if not m:
		return full
	root, suf = m.group(1), m.group(2).lower()
	base = {
		"ова": "ов",
		"єва": "єв",
		"ева": "ев",
		"іна": "ін",
		"їна": "їн",
	}[suf]
	if case == "genitive":
		return root + base + "ої"
	if case == "dative":
		return root + base + "ій"
	if case == "accusative":
		return root + base + "у"
	if case == "instrumental":
		return root + base + "ою"
	if case == "locative":
		return root + base + "ій"
	if case == "vocative":
		return full
	return full


def _f_surname_a_ya(full: str, case: CaseKey, variant: Variant) -> str:
	# Special patterns first
	if re.search(r"(?i)(?:о|є|е)ва$", full) or re.search(r"(?i)[ії]на$", full):
		return _f_surname_special_slavic(full, case, variant)
	# Generic -а/-я
	base = full[:-1]
	if case == "genitive":
		return base + ("и" if full.endswith("а") else "і")
	if case == "dative":
		return base + "і"
	if case == "accusative":
		return base + ("у" if full.endswith("а") else "ю")
	if case == "instrumental":
		return base + ("ою" if full.endswith("а") else "ею")
	if case == "locative":
		return base + "і"
	if case == "vocative":
		return full
	return full


def _invariable(full: str, case: CaseKey, variant: Variant) -> str:
	return full


SURNAME_RULES: list[Rule] = [
	Rule("m_adj_iy", "surname", "m", _re(r".*[іи]й$"), 10, _m_surname_adj_iy),
	Rule("m_enko", "surname", "m", _re(r".+енко$"), 20, _m_surname_enko_ko),
	Rule("m_ko", "surname", "m", _re(r".+ко$"), 21, _m_surname_enko_ko),
	Rule("m_etz", "surname", "m", _re(r".+ець$"), 22, _m_surname_etz),
	Rule("m_soft", "surname", "m", _re(r".*(?:[нл]ь|й)$"), 30, _m_surname_soft),
	Rule("m_ch_shch", "surname", "m", _re(r".*[чщ]$"), 40, _m_surname_ch_shch),
	Rule("m_hard", "surname", "m", _re(r".+[^аеєиіїоуюяьй]$"), 90, _m_surname_hard),
	Rule("f_a_ya", "surname", "f", _re(r".+[ая]$"), 10, _f_surname_a_ya),
	Rule("f_cons_invar", "surname", "f", _re(r".+[^аеєиіїоуюя]$"), 90, _invariable),
]


# Given names (masculine common patterns)

def _m_given_an(full: str, case: CaseKey, variant: Variant) -> str:
	if case in ("genitive", "accusative"):
		return full + "а"
	if case == "dative":
		return (full + "ові") if variant == "long" else (full + "у")
	if case == "instrumental":
		return full + "ом"
	if case == "locative":
		return full + "ові"
	if case == "vocative":
		return full + "е"
	return full


def _m_given_iy(full: str, case: CaseKey, variant: Variant) -> str:
	base = full[:-2]
	if case in ("genitive", "accusative"):
		return base + "ія"
	if case == "dative" or case == "locative":
		return base + "ію"
	if case == "instrumental":
		return base + "ієм"
	if case == "vocative":
		return base + "ію"
	return full


def _f_given_a_ya(full: str, case: CaseKey, variant: Variant) -> str:
	base = full[:-1]
	if case == "genitive":
		return base + ("и" if full.endswith("а") else "і")
	if case == "dative":
		return base + "і"
	if case == "accusative":
		return base + ("у" if full.endswith("а") else "ю")
	if case == "instrumental":
		return base + ("ою" if full.endswith("а") else "ею")
	if case == "locative":
		return base + "і"
	if case == "vocative":
		return full
	return full


def _patr_m_ovich(full: str, case: CaseKey, variant: Variant) -> str:
	if case in ("genitive", "accusative"):
		return full + "а"
	if case == "dative":
		return full + "у"
	if case == "instrumental":
		return full + "ем"
	if case == "locative":
		return full + "у"
	if case == "vocative":
		return full + "у"
	return full


def _patr_f_ivna(full: str, case: CaseKey, variant: Variant) -> str:
	base = full[:-1]
	if case == "genitive":
		return base + "и"
	if case == "dative":
		return base + "і"
	if case == "accusative":
		return base + "у"
	if case == "instrumental":
		return base + "ою"
	if case == "locative":
		return base + "і"
	if case == "vocative":
		return full
	return full


GIVEN_RULES: list[Rule] = [
	Rule("m_given_iy", "given", "m", _re(r".*ій$"), 10, _m_given_iy),
	Rule("m_given_an", "given", "m", _re(r".*ан$"), 20, _m_given_an),
	Rule("f_given_a_ya", "given", "f", _re(r".+[ая]$"), 10, _f_given_a_ya),
]

PATR_RULES: list[Rule] = [
	Rule("m_patr_ovich", "patronymic", "m", _re(r".*ович$"), 10, _patr_m_ovich),
	Rule("f_patr_ivna", "patronic", "f", _re(r".*івна$"), 10, _patr_f_ivna),
]


def find_rule(name: str, rules: list[Rule], gender: Optional[Gender]) -> Optional[Rule]:
	candidates = [r for r in rules if r.gender in (None, gender)]
	for r in sorted(candidates, key=lambda x: x.priority):
		if r.pattern.match(name):
			return r
	return None