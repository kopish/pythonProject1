from __future__ import annotations

from typing import Dict, Optional, TypedDict
from pydantic import BaseModel
import yaml
import os


class GenderForms(TypedDict, total=False):
	long: str
	short: str


class CustomForms(TypedDict, total=False):
	m: GenderForms
	f: GenderForms


class ExceptionsConfig(BaseModel):
	invariable_feminine: list[str] = []
	custom_forms: Dict[str, CustomForms] = {}


_DEF_PATH = os.path.join(os.path.dirname(__file__), "exceptions.yml")


def load_exceptions(path: Optional[str] = None) -> ExceptionsConfig:
	cfg_path = path or _DEF_PATH
	if not os.path.exists(cfg_path):
		return ExceptionsConfig()
	with open(cfg_path, "r", encoding="utf-8") as f:
		data = yaml.safe_load(f) or {}
	return ExceptionsConfig.model_validate(data)