"""
Data model for BLDC motor input parameters.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class MotorParameters:
    """
    Stores all input parameters required for a BLDC motor simulation.
    """

    rated_voltage: float
    rated_current: float
    kv_constant: float
    pole_pairs: int
    wheel_diameter: float
    vehicle_mass: float

    gear_ratio: float = 1.0
    controller_efficiency: float = 0.95
    motor_efficiency: float = 0.90