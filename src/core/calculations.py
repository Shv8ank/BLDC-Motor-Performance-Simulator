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

    Formula:
        P = V × I

    Args:
        voltage: Supply voltage (V)
        current: Supply current (A)

    Returns:
        Electrical power (W)
    """
    return voltage * current


def calculate_motor_rpm(
    voltage: float,
    kv_constant: float,
) -> float:
    """
    Calculate no-load motor speed.

    Formula:
        RPM = KV × Voltage

    Args:
        voltage: Supply voltage (V)
        kv_constant: Motor KV rating (RPM/V)

    Returns:
        Motor speed (RPM)
    """
    return voltage * kv_constant


def calculate_angular_velocity(
    rpm: float,
) -> float:
    """
    Convert RPM to angular velocity.

    Formula:
        ω = (2π × RPM) / 60

    Args:
        rpm: Motor speed (RPM)

    Returns:
        Angular velocity (rad/s)
    """
    return (2 * pi * rpm) / 60


def calculate_mechanical_power(
    electrical_power: float,
    motor_efficiency: float,
) -> float:
    """
    Calculate mechanical output power.

    Formula:
        P_mechanical = P_electrical × η

    Args:
        electrical_power: Electrical input power (W)
        motor_efficiency: Motor efficiency (0-1)

    Returns:
        Mechanical output power (W)
    """
    return electrical_power * motor_efficiency


def calculate_torque(
    mechanical_power: float,
    angular_velocity: float,
) -> float:
    """
    Calculate motor torque.

    Formula:
        T = P / ω

    Args:
        mechanical_power: Mechanical output power (W)
        angular_velocity: Angular velocity (rad/s)

    Returns:
        Motor torque (N·m)
    """
    if angular_velocity == 0:
        return 0.0

    return mechanical_power / angular_velocity