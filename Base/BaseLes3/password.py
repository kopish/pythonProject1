import string


def password_strenght(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue
    if count == 3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'
    # if all(e in digits for e in value) or all(
    #         e in lowers for e in value) or all(e in uppers for e in value):
    #     return 'Weak'
    # if any(e in digits for e in value) or any(
    #         e in lowers for e in value) or any(e in uppers for e in value):
    #     return 'Very Good'
    # if (any(e in digits for e in value) and any(
    #         e in lowers for e in value)) or (any(
    #     e in digits for e in value) and any(
    #     e in uppers for e in value)) or (any(
    #     e in lowers for e in value) and any(
    #     e in uppers for e in value)):
    # return "Good"


if __name__ == '__main__':
    assert password_strenght('') == 'Too Weak'
    assert password_strenght('dfydynu') == 'Too Weak'
    assert password_strenght('1234567') == 'Too Weak'
    assert password_strenght('GHJUYTR') == 'Too Weak'
    assert password_strenght('yuhJIU8') == 'Too Weak'
    assert password_strenght('12345678') == 'Weak'
    assert password_strenght('dfstyjydynu') == 'Weak'
    assert password_strenght('1234556367') == 'Weak'
    assert password_strenght('GHJUYTJHVRE') == 'Weak'
    assert password_strenght('8491ghvj') == 'Good'
    assert password_strenght('8491IHVIJ') == 'Good'
    assert password_strenght('iervbOIYVYIT') == 'Good'
    assert password_strenght('1234uyvF') == 'Very Good'
    assert password_strenght('oierUHBY789') == 'Very Good'
    assert password_strenght('123485lJ') == 'Very Good'
    assert password_strenght('iyhebv651UYBU') == 'Very Good'
