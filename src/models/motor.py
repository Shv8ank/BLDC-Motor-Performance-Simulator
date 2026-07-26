from dataclasses import dataclass


@dataclass(slots=True)
class MotorParameters:
    rated_voltage: float
    rated_current: float

    rated_power: float

    rated_speed: float      # RPM
    max_speed: float        # RPM

    rated_torque: float     # Nm
    peak_torque: float      # Nm

    wheel_diameter: float
    vehicle_mass: float

    controller_efficiency: float
    motor_efficiency: float