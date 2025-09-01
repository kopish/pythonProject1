from __future__ import annotations

from typing import Optional, Tuple, Literal
import regex as re

UA_APOSTROPHES = "'ʼ’`"
HYPHEN = "-"
SPACE = " "

CaseKey = Literal[
	"nominative", "genitive", "dative", "accusative", "instrumental", "locative", "vocative",
]


def split_full_name(text: str) -> Tuple[str, Optional[str], Optional[str]]:
	text = text.strip()
	parts = [p for p in re.split(r"\s+", text) if p]
	if not parts:
		return "", None, None
	if len(parts) == 1:
		return parts[0], None, None
	if len(parts) == 2:
		return parts[0], parts[1], None
	return parts[0], parts[1], " ".join(parts[2:])


def is_all_caps(text: str) -> bool:
	letters = re.findall(r"\p{L}", text)
	return bool(letters) and all(ch.upper() == ch for ch in letters)


def is_title_case(text: str) -> bool:
	def seg_title(seg: str) -> bool:
		if not seg:
			return True
		letters = re.findall(r"\p{L}", seg)
		if not letters:
			return True
		return seg[:1] == seg[:1].upper() and seg[1:] == seg[1:].lower()

	segments = re.split(rf"[^\p{{L}}{re.escape(UA_APOSTROPHES + HYPHEN)}]+", text)
	segments = [s for s in segments if s]
	return all(seg_title(s) for s in segments) if segments else False


def title_like(text: str) -> str:
	def title_word(word: str) -> str:
		subs = word.split(HYPHEN)
		titled_subs = [sub[:1].upper() + sub[1:].lower() if sub else sub for sub in subs]
		return HYPHEN.join(titled_subs)

	tokens = re.split(r"(\s+)", text)
	for i in range(0, len(tokens), 2):
		tokens[i] = title_word(tokens[i])
	return "".join(tokens)


def apply_case_like(example: str, text: str, keep_case: bool = True) -> str:
	if not keep_case:
		return title_like(text)
	if is_all_caps(example):
		return text.upper()
	if is_title_case(example):
		return title_like(text)
	return text


def normalize_apostrophes(text: str) -> str:
	return re.sub(rf"[{re.escape(UA_APOSTROPHES)}]", "’", text)


def split_hyphenated(text: str) -> list[str]:
	return text.split(HYPHEN) if HYPHEN in text else [text]


def join_hyphenated(parts: list[str]) -> str:
	return HYPHEN.join(parts)