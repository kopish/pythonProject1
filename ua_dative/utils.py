from __future__ import annotations

from typing import Literal, Optional, Tuple
import regex as re

UA_APOSTROPHES = "'ʼ’`"
HYPHEN = "-"
SPACE = " "


def split_full_name(text: str) -> Tuple[str, Optional[str], Optional[str]]:
	"""Split into surname, given name, patronymic (if present).

	Strategy: treat the first token as surname, second as given name, third+ as patronymic tail.
	Supports hyphens within tokens.
	"""
	text = text.strip()
	if not text:
		return "", None, None
	parts = [p for p in re.split(r"\s+", text) if p]
	if len(parts) == 1:
		return parts[0], None, None
	if len(parts) == 2:
		return parts[0], parts[1], None
	return parts[0], parts[1], " ".join(parts[2:])


def is_all_caps(text: str) -> bool:
	letters = re.findall(r"\p{L}", text)
	return bool(letters) and all(ch.upper() == ch for ch in letters)


def is_title_case(text: str) -> bool:
	# Consider hyphenated and apostrophized surnames: every alphabetic segment title-cased
	def seg_title(seg: str) -> bool:
		if not seg:
			return True
		letters = re.findall(r"\p{L}", seg)
		if not letters:
			return True
		return seg[:1] == seg[:1].upper() and seg[1:] == seg[1:].lower()

	# Split on non-letters except apostrophes and hyphens
	segments = re.split(rf"[^\p{{L}}{re.escape(UA_APOSTROPHES + HYPHEN)}]+", text)
	segments = [s for s in segments if s]
	return all(seg_title(s) for s in segments) if segments else False


def apply_case_like(example: str, text: str, keep_case: bool = True) -> str:
	"""Apply casing of example to text.

	- If keep_case is False: return Title Case of text (per-part)
	- If example is ALL CAPS: return text uppercased
	- If example is Title Case: return title-cased per hyphen/apostrophe parts
	- Else: return text as-is
	"""
	if not text:
		return text

	if not keep_case:
		return title_like(text)

	if is_all_caps(example):
		return text.upper()
	if is_title_case(example):
		return title_like(text)
	return text


def title_like(text: str) -> str:
	# Title-case separately for hyphenated parts, keep apostrophes
	def title_word(word: str) -> str:
		# Handle inner apostrophes e.g., П'ятенко
		if not word:
			return word
		# Split at hyphen and title-case each subpart
		subs = word.split(HYPHEN)
		titled_subs = [sub[:1].upper() + sub[1:].lower() if sub else sub for sub in subs]
		return HYPHEN.join(titled_subs)

	tokens = re.split(r"(\s+)", text)
	for i, tok in enumerate(tokens):
		if i % 2 == 0:
			tokens[i] = title_word(tok)
	return "".join(tokens)


def normalize_apostrophes(text: str) -> str:
	return re.sub(rf"[{re.escape(UA_APOSTROPHES)}]", "’", text)


def split_hyphenated(text: str) -> list[str]:
	return text.split(HYPHEN) if HYPHEN in text else [text]


def join_hyphenated(parts: list[str]) -> str:
	return HYPHEN.join(parts)


def strip_non_letters_edges(text: str) -> str:
	return re.sub(r"^\W+|\W+$", "", text)


def endswith_any(text: str, suffixes: tuple[str, ...]) -> bool:
	return any(text.endswith(suf) for suf in suffixes)


def last_letter(text: str) -> str:
	m = re.search(r"\p{L}(?=[^\p{L}]*$)", text)
	return m.group(0) if m else ""


Gender = Literal["m", "f"]
Variant = Literal["short", "long", "auto"]