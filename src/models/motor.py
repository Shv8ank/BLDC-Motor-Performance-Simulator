from dataclasses import dataclass


@dataclass(slots=True)
class MotorParameters:
    rated_voltage: float
    rated_current: float

    rated_power: float

    rated_speed: float
    max_speed: float

    rated_torque: float
    peak_torque: float

    wheel_diameter: float
    vehicle_mass: float

    battery_voltage: float
    battery_capacity: float

    controller_efficiency: float
    motor_efficiency: float