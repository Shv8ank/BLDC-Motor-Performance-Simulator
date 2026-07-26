"""
Core engineering calculations for the BLDC Motor Performance Simulator.
"""

from math import pi


def calculate_electrical_power(
    voltage: float,
    current: float,
) -> float:
    """
    Calculate electrical input power.
    """
    return voltage * current


def calculate_motor_rpm(
    voltage: float,
    kv_constant: float,
) -> float:
    """
    Calculate no-load motor speed.
    """
    return voltage * kv_constant


def calculate_angular_velocity(
    rpm: float,
) -> float:
    """
    Convert RPM to angular velocity.
    """
    return (2 * pi * rpm) / 60


def calculate_mechanical_power(
    electrical_power: float,
    motor_efficiency: float,
) -> float:
    """
    Calculate mechanical output power.
    """
    return electrical_power * motor_efficiency


def calculate_torque(
    mechanical_power: float,
    angular_velocity: float,
) -> float:
    """
    Calculate motor torque.
    """
    if angular_velocity == 0:
        return 0.0

    return mechanical_power / angular_velocity

def calculate_wheel_force(
    torque: float,
    wheel_diameter: float,
) -> float:
    """
    Calculate tractive force at the wheel.
    """
    wheel_radius = wheel_diameter / 2

    if wheel_radius == 0:
        return 0.0

    return torque / wheel_radius


def calculate_vehicle_speed(
    wheel_rpm: float,
    wheel_diameter: float,
) -> float:
    """
    Calculate theoretical vehicle speed (km/h).
    """
    wheel_circumference = pi * wheel_diameter

    speed_m_per_min = wheel_rpm * wheel_circumference

    speed_km_per_h = (speed_m_per_min * 60) / 1000

    return speed_km_per_h



