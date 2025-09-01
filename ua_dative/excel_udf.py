from __future__ import annotations

from typing import Literal, Optional

try:
	import xlwings as xw
except Exception:  # pragma: no cover - optional at runtime
	xw = None

from .engine import to_dative
from .names_loader import load_names, detect_gender_by_given_name
from .utils import split_full_name


_WARN_STATE: dict[int, str] = {}


def _set_warn(msg: str) -> None:
	# store a single warn; in real use, could be keyed by caller context
	_WARN_STATE[0] = msg


if xw is not None:
	@xw.func(category="UA Dative")
	def UA_DATIVE(surname: str, gender: str = "", variant: str = "auto", keep_case: bool = True) -> str:  # type: ignore[misc]
		g: Literal["m", "f", "auto"]
		g = "auto" if gender == "" else gender  # type: ignore[assignment]
		try:
			res = to_dative(str(surname), g, variant, bool(keep_case))
			if g == "auto":
				# warn if unchanged and gender ambiguous
				s, given, _ = split_full_name(str(surname))
				if given:
					names = load_names()
					if detect_gender_by_given_name(given, names) is None and res == s:
						_set_warn("Gender ambiguous: provide gender for precise result")
			return res
		except Exception as e:  # pragma: no cover - Excel displays error strings
			return f"#UA_ERR: {e}"

	@xw.func(category="UA Dative")
	def UA_WARN() -> str:  # type: ignore[misc]
		return _WARN_STATE.get(0, "")