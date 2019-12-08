# https://codechalleng.es/bites/169/


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()
    if type(value) != int and type(value) != float:
        raise TypeError

    if fmt != "cm" and fmt != "in":
        raise ValueError

    if fmt == "cm":
        return round((value * 2.54), 4)

    elif fmt == "in":
        return round((value / 2.54), 4)
