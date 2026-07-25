import pytest

from src.core.validators import validate_motor_parameters
from src.models.motor import MotorParameters


def create_motor():
    return MotorParameters(
        rated_voltage=48,
        rated_current=30,
        kv_constant=320,
        pole_pairs=15,
        wheel_diameter=0.30,
        vehicle_mass=120,
        gear_ratio=1.0,
        controller_efficiency=0.95,
        motor_efficiency=0.90,
    )


def test_valid_motor():
    validate_motor_parameters(create_motor())


def test_invalid_voltage():
    motor = create_motor()
    motor.rated_voltage = -48

    with pytest.raises(ValueError):
        validate_motor_parameters(motor)


def test_invalid_efficiency():
    motor = create_motor()
    motor.motor_efficiency = 1.5

    with pytest.raises(ValueError):
        validate_motor_parameters(motor)