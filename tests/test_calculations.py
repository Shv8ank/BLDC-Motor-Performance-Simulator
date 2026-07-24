from math import isclose, pi

from src.core.calculations import (
    calculate_angular_velocity,
    calculate_electrical_power,
    calculate_mechanical_power,
    calculate_motor_rpm,
    calculate_torque,
)


def test_calculate_electrical_power():
    assert calculate_electrical_power(48, 30) == 1440


def test_calculate_motor_rpm():
    assert calculate_motor_rpm(48, 320) == 15360


def test_calculate_angular_velocity():
    expected = (2 * pi * 15360) / 60
    result = calculate_angular_velocity(15360)

    assert isclose(result, expected, rel_tol=1e-9)


def test_calculate_mechanical_power():
    assert calculate_mechanical_power(1440, 0.90) == 1296


def test_calculate_torque():
    omega = calculate_angular_velocity(15360)
    mechanical_power = calculate_mechanical_power(1440, 0.90)

    torque = calculate_torque(
        mechanical_power,
        omega,
    )

    assert isclose(torque, 0.8057, rel_tol=1e-3)


def test_calculate_torque_zero_speed():
    assert calculate_torque(1000, 0) == 0.0