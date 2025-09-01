from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal, Optional
import regex as re

from .utils import Gender, Variant, endswith_any


@dataclass(frozen=True)
class Rule:
	name: str
	gender: Literal["m", "f"]
	pattern: re.Pattern[str]
	priority: int
	apply: Callable[[str, Variant], str]


def _re(s: str) -> re.Pattern[str]:
	return re.compile(s, re.IGNORECASE)


# Masculine rules

def apply_m_hard_consonant(base: str, variant: Variant) -> str:
	if variant == "short":
		return base + "у"
	return base + "ові"


def apply_m_soft_affric(full: str, variant: Variant) -> str:
	# base is without final й/ь
	base = full[:-1]
	if variant == "short":
		return base + "ю"
	if full.endswith("ай"):
		return base + "єві"
	return base + "еві"


def apply_m_enko_ko(full: str, variant: Variant) -> str:
	stem = full[:-1]
	if variant == "short":
		return stem + "у"
	return stem + "ові"


def apply_m_adj_like(base: str, variant: Variant) -> str:
	return base + "ому"


def apply_m_ech_etz(full: str, variant: Variant) -> str:
	# -ець: remove 'ець'
	stem = full[:-3]
	if variant == "short":
		return stem + "цю"
	return stem + "цеві"


def apply_m_cz_zc_ch_shch(full: str, variant: Variant) -> str:
	if full.endswith("ч") or full.endswith("щ"):
		if variant == "short":
			return full + "у"
		return full + "еві"
	if full.endswith("ць") or full.endswith("зь"):
		stem = full[:-1]
		if variant == "short":
			return stem + "ю"
		return stem + "еві"
	if variant == "short":
		return full + "у"
	return full + "еві"


# Feminine rules

def apply_f_a_ya(base: str, variant: Variant) -> str:
	return base + "ій"


def invariable(base: str, variant: Variant) -> str:
	return base


RULES: list[Rule] = [
	Rule(
		name="m_adj_like_iy",
		gender="m",
		pattern=_re(r"(?i).*[іи]й$"),
		priority=10,
		apply=lambda s, v: apply_m_adj_like(s[:-2], v),
	),
	Rule(
		name="m_suffix_enko",
		gender="m",
		pattern=_re(r"(?i).+енко$"),
		priority=20,
		apply=lambda s, v: apply_m_enko_ko(s, v),
	),
	Rule(
		name="m_suffix_ko",
		gender="m",
		pattern=_re(r"(?i).+ко$"),
		priority=21,
		apply=lambda s, v: apply_m_enko_ko(s, v),
	),
	Rule(
		name="m_soft_affric",
		gender="m",
		pattern=_re(r"(?i).*(?:[й]|[нл]ь)$"),
		priority=30,
		apply=lambda s, v: apply_m_soft_affric(s, v),
	),
	Rule(
		name="m_end_etz",
		gender="m",
		pattern=_re(r"(?i).+ець$"),
		priority=35,
		apply=lambda s, v: apply_m_ech_etz(s, v),
	),
	Rule(
		name="m_end_cz_zc_ch_shch",
		gender="m",
		pattern=_re(r"(?i).*(?:[зс]ь|[чщ])$"),
		priority=40,
		apply=lambda s, v: apply_m_cz_zc_ch_shch(s, v),
	),
	Rule(
		name="m_hard_cons",
		gender="m",
		pattern=_re(r"(?i).+[^аеєиіїоуюяьй]$"),
		priority=90,
		apply=lambda s, v: apply_m_hard_consonant(s, v),
	),
	# Feminine
	Rule(
		name="f_adj_like_a",
		gender="f",
		pattern=_re(r"(?i).+[ая]$"),
		priority=10,
		apply=lambda s, v: apply_f_a_ya(s[:-1], v),
	),
	Rule(
		name="f_invariable_cons",
		gender="f",
		pattern=_re(r"(?i).+[^аеєиіїоуюя]$"),
		priority=90,
		apply=lambda s, v: invariable(s, v),
	),
]


def find_rule(surname: str, gender: Gender) -> Optional[Rule]:
	for rule in sorted((r for r in RULES if r.gender == gender), key=lambda x: x.priority):
		if rule.pattern.match(surname):
			return rule
	return None