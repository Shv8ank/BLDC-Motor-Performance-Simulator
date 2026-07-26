"""
Validation utilities for the EV Hub Motor Performance Simulator.
"""

from src.models.motor import MotorParameters


def validate_motor_parameters(motor: MotorParameters) -> None:
    """
    Validate motor parameters before simulation.

    Raises
    ------
    ValueError
        If any parameter is invalid.
    """

    if motor.rated_voltage <= 0:
        raise ValueError("Rated voltage must be greater than zero.")

    if motor.rated_current <= 0:
        raise ValueError("Rated current must be greater than zero.")

    if motor.rated_power <= 0:
        raise ValueError("Rated power must be greater than zero.")

    if motor.rated_speed <= 0:
        raise ValueError("Rated speed must be greater than zero.")

    if motor.max_speed <= 0:
        raise ValueError("Maximum speed must be greater than zero.")

    if motor.rated_torque <= 0:
        raise ValueError("Rated torque must be greater than zero.")

    if motor.peak_torque <= 0:
        raise ValueError("Peak torque must be greater than zero.")

    if motor.wheel_diameter <= 0:
        raise ValueError("Wheel diameter must be greater than zero.")

    if motor.vehicle_mass <= 0:
        raise ValueError("Vehicle mass must be greater than zero.")

    if not (0 < motor.controller_efficiency <= 1):
        raise ValueError(
            "Controller efficiency must be between 0 and 1."
        )

    if not (0 < motor.motor_efficiency <= 1):
        raise ValueError(
            "Motor efficiency must be between 0 and 1."
        )