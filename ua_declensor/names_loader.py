from __future__ import annotations

from typing import Optional
from pydantic import BaseModel
import yaml
import os
import regex as re


class NamesConfig(BaseModel):
	male: list[str] = []
	female: list[str] = []


_DEF_PATH = os.path.join(os.path.dirname(__file__), "names.yml")


def load_names(path: Optional[str] = None) -> NamesConfig:
	cfg_path = path or _DEF_PATH
	if not os.path.exists(cfg_path):
		return NamesConfig()
	with open(cfg_path, "r", encoding="utf-8") as f:
		data = yaml.safe_load(f) or {}
	return NamesConfig.model_validate(data)


def _normalize_name(name: str) -> str:
	return re.sub(r"\s+", " ", name.strip()).casefold()


def detect_gender_by_given_name(given: str, names: NamesConfig) -> Optional[str]:
	g = _normalize_name(given)
	male = {n.casefold() for n in names.male}
	female = {n.casefold() for n in names.female}
	if g in male and g in female:
		return None
	if g in male:
		return "m"
	if g in female:
		return "f"
	return None