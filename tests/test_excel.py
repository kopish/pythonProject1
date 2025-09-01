import pytest

from ua_dative import to_dative


def test_udf_logic_like():
	# We don't import xlwings in tests; just ensure engine works as UDF would call
	assert to_dative("Коваль", gender="m", variant="long") == "Ковалеві"