from math import pi


def calculate_electrical_power(voltage: float, current: float) -> float:
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


def calculate_motor_rpm(voltage: float, kv_constant: float) -> float:
    """
    Calculate ideal no-load motor speed.

    Formula:
        RPM = KV × Voltage

    Args:
        voltage: Supply voltage (V)
        kv_constant: Motor KV rating (RPM/V)

    Returns:
        Motor speed (RPM)
    """
    return voltage * kv_constant


def calculate_angular_velocity(rpm: float) -> float:
    """
    Convert RPM to angular velocity.

    Formula:
        ω = 2π × RPM / 60

    Args:
        rpm: Motor speed (RPM)

    Returns:
        Angular velocity (rad/s)
    """
    return (2 * pi * rpm) / 60