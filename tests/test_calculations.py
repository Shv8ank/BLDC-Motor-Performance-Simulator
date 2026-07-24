from math import isclose, pi

from src.core.calculations import (
    calculate_angular_velocity,
    calculate_electrical_power,
    calculate_motor_rpm,
)


def test_calculate_electrical_power():
    assert calculate_electrical_power(48, 30) == 1440


def test_calculate_motor_rpm():
    assert calculate_motor_rpm(48, 320) == 15360


def test_calculate_angular_velocity():
    expected = (2 * pi * 15360) / 60
    assert isclose(
        calculate_angular_velocity(15360),
        expected,
        rel_tol=1e-9,
    )