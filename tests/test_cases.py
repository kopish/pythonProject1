import pytest

from ua_declensor.engine import decline_full_name_all_cases


def assert_cases(full_name: str, gender: str, expected: dict[str, str]):
	res = decline_full_name_all_cases(full_name, gender=gender)
	for k, v in expected.items():
		assert res[k] == v


def test_male_fullname_basic():
	cases = decline_full_name_all_cases("Петренко Іван Іванович", gender="m")
	assert cases["nominative"] == "Іван Петренко Іванович"
	assert cases["genitive"].startswith("Івана Петренка")
	assert "Івановича" in cases["genitive"]
	assert "Іванові" in cases["dative"] or "Івану" in cases["dative"]
	assert "Петренкові" in cases["dative"] or "Петренку" in cases["dative"]
	# Instrumental should contain: Іваном ... Петренком ... Івановичем
	assert "Іваном" in cases["instrumental"]
	assert "Петренком" in cases["instrumental"]
	assert "Івановичем" in cases["instrumental"]


def test_female_fullname_basic():
	cases = decline_full_name_all_cases("Іванова Олена Іванівна", gender="f")
	assert cases["nominative"].startswith("Олена Іванова")
	assert cases["genitive"].startswith("Олени Іванової")
	assert "Іванівни" in cases["genitive"]
	assert cases["dative"].startswith("Олені Івановій")
	assert cases["accusative"].startswith("Олену Іванову")
	assert cases["instrumental"].startswith("Оленою Івановою")
	assert cases["locative"].startswith("Олені Івановій")


@pytest.mark.parametrize(
	"surname,expected_dative",
	[
		("Коваль", "Ковалеві"),
		("Мельник", "Мельникові"),
		("Гончарук", "Гончарукові"),
		("Деркач", "Деркачеві"),
		("Гайдай", "Гайдаєві"),
		("Ставець", "Ставцеві"),
		("Петренко", "Петренкові"),
	],
)
def test_surname_dative_long(surname, expected_dative):
	cases = decline_full_name_all_cases(f"{surname} Іван Іванович", gender="m")
	assert expected_dative.split()[0] in cases["dative"]


@pytest.mark.parametrize(
	"given,expected_vocative",
	[
		("Іван", "Іване"),
		("Андрій", "Андрію"),
	],
)
def test_given_vocative(given, expected_vocative):
	cases = decline_full_name_all_cases(f"Коваль {given} Іванович", gender="m")
	assert cases["vocative"].startswith(expected_vocative)


def test_apostrophe_and_hyphen():
	cases = decline_full_name_all_cases("П’ятенко-Іванов Іван Іванович", gender="m")
	assert "П’ятенкові-Іванову" in cases["dative"]


def test_case_preservation_all_caps():
	cases = decline_full_name_all_cases("КОВАЛЬ ІВАН ІВАНОВИЧ", gender="m", keep_case=True)
	for v in cases.values():
		assert v.upper() == v


@pytest.mark.parametrize(
	"full_name,gender",
	[
		("Петренко Іван Іванович", "m"),
		("Іванова Олена Іванівна", "f"),
		("Гордієнко Юрій Петрович", "m"),
		("Руденко-Іванов Андрій Сергійович", "m"),
		("Руденко-Іванова Оксана Сергіївна", "f"),
	],
)
def test_many_samples(full_name, gender):
	cases = decline_full_name_all_cases(full_name, gender=gender)
	assert cases["nominative"]
	assert cases["genitive"]
	assert cases["dative"]
	assert cases["accusative"]
	assert cases["instrumental"]
	assert cases["locative"]
	assert cases["vocative"]