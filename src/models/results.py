"""
Data model for simulation results.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SimulationResults:
    """
    Stores the complete output of a hub motor simulation.
    """

    electrical_power: float
    mechanical_power: float

    motor_rpm: float
    wheel_rpm: float
    angular_velocity: float

    torque: float
    wheel_force: float

    vehicle_speed: float
    estimated_top_speed: float

    overall_efficiency: float