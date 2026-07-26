"""
Drivetrain calculations for the EV Performance Simulator.
"""

from math import pi


def calculate_wheel_rpm(
    motor_rpm: float,
    gear_ratio: float,
) -> float:
    """
    Calculates wheel RPM after gear reduction.
    """
    if gear_ratio <= 0:
        raise ValueError("Gear ratio must be greater than zero.")

    return motor_rpm / gear_ratio


def calculate_wheel_torque(
    motor_torque: float,
    gear_ratio: float,
    drivetrain_efficiency: float = 0.95,
) -> float:
    """
    Calculates torque available at the wheel after the drivetrain.
    """

    return (
        motor_torque
        * gear_ratio
        * drivetrain_efficiency
    )


def calculate_wheel_force(
    wheel_torque: float,
    wheel_diameter: float,
) -> float:
    """
    Converts wheel torque into tractive force.
    """

    radius = wheel_diameter / 2

    if radius <= 0:
        return 0.0

    return wheel_torque / radius


def calculate_vehicle_speed(
    wheel_rpm: float,
    wheel_diameter: float,
) -> float:
    """
    Converts wheel RPM into vehicle speed (km/h).
    """

    circumference = pi * wheel_diameter

    speed_m_per_min = (
        wheel_rpm
        * circumference
    )

    return (
        speed_m_per_min
        * 60
        / 1000
    )