import pytest

from ua_dative import to_dative


@pytest.mark.parametrize(
	"surname,variant,expected",
	[
		("Петренко", "long", "Петренкові"),
		("Петренко", "short", "Петренку"),
		("Гордієнко", "long", "Гордієнкові"),
		("Гордієнко", "short", "Гордієнку"),
		("Коваль", "long", "Ковалеві"),
		("Коваль", "short", "Ковалю"),
		("Мельник", "long", "Мельникові"),
		("Мельник", "short", "Мельнику"),
		("Гончарук", "long", "Гончарукові"),
		("Гончарук", "short", "Гончаруку"),
		("Деркач", "long", "Деркачеві"),
		("Деркач", "short", "Деркачу"),
		("Гайдай", "long", "Гайдаєві"),
		("Гайдай", "short", "Гайдаю"),
		("Ставець", "long", "Ставцеві"),
		("Ставець", "short", "Ставцю"),
	],
)
def test_masculine_basic(surname, variant, expected):
	assert to_dative(surname, gender="m", variant=variant) == expected


@pytest.mark.parametrize(
	"surname,expected",
	[
		("Іванова", "Івановій"),
		("Польова", "Польовій"),
		("Ганніча", "Ганнічій"),
	],
)
def test_feminine_a_ya(surname, expected):
	assert to_dative(surname, gender="f", variant="long") == expected


def test_feminine_invariable_consonant():
	assert to_dative("Петренко", gender="f", variant="long") == "Петренко"


def test_hyphenated_m():
	assert to_dative("Руденко-Іванов", gender="m", variant="long") == "Руденкові-Іванову"


def test_hyphenated_f():
	assert to_dative("Руденко-Іванова", gender="f", variant="long") == "Руденко-Івановій"


def test_apostrophe_long():
	assert to_dative("П’ятенко", gender="m", variant="long") == "П’ятенкові"


def test_case_preservation():
	assert to_dative("КОВАЛЬ", gender="m", variant="short") == "КОВАЛЮ"
	assert to_dative("Коваль", gender="m", variant="short") == "Ковалю"
	assert to_dative("коваль", gender="m", variant="long") == "ковалеві"


def test_full_name_gender_auto_known():
	# Given name male
	assert to_dative("Коваль Андрій", gender="auto", variant="long") == "Ковалеві"


def test_full_name_gender_auto_ambiguous_returns_unchanged_surname_cased():
	res = to_dative("Коваль Алекс", gender="auto", variant="long")
	assert res == "Коваль"  # unchanged due to ambiguous name