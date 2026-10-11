"""Ядро конвертера единиц: длина, масса, температура."""

from .constants import ABSOLUTE_ZERO, UNITS
from .errors import ConverterError
from .validator import validate_units


def convert(val: float, from_unit: str, to_unit: str) -> float:
    """Перевод значений."""
    from_unit, to_unit = validate_units(from_unit, to_unit)

    group_from, factor_from = UNITS[from_unit]
    group_to, factor_to = UNITS[to_unit]

    if group_from == "temp":
        cels = to_cels(val, from_unit)
        if cels < ABSOLUTE_ZERO:
            raise ConverterError("Температура ниже абсолютного нуля")
        return from_cels(cels, to_unit)


    base_val = val*factor_from
    return base_val/factor_to


def to_cels(val: float, unit: str) -> float:
    """Переводит температуру в Цельсий."""
    if unit == "c":
        return val
    if unit == "f":
        return (val-32)*5/9
    if unit == "k":
        return val - 273.15
    raise ConverterError(f"Неизвестная единица температуры: {unit}")


def from_cels(cels: float, unit: str) -> float:
    """Переводит температуру из Цельсия в целевую единицу."""
    if unit == "c":
        return cels
    if unit == "f":
        return cels * 9/5+32
    if unit == "k":
        return cels + 273.15
    raise ConverterError(f"Неизвестная единица температуры: {unit}")