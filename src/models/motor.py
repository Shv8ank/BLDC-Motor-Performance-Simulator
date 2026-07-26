from dataclasses import dataclass


@dataclass(slots=True)
class MotorParameters:
    """
    Stores all user-defined BLDC motor parameters.
    """

    rated_voltage: float
    rated_current: float
    kv_constant: float
    pole_pairs: int
    wheel_diameter: float
    vehicle_mass: float
    controller_efficiency: float = 0.95
    motor_efficiency: float = 0.90