"""
Simulation engine for the BLDC Motor Performance Simulator.
"""

from src.models.motor import MotorParameters
from src.models.results import SimulationResults
from src.core.validators import validate_motor_parameters

from src.core.calculations import (
    calculate_angular_velocity,
    calculate_electrical_power,
    calculate_estimated_top_speed,
    calculate_mechanical_power,
    calculate_motor_rpm,
    calculate_torque,
    calculate_vehicle_speed,
    calculate_wheel_force,
    calculate_wheel_rpm,
)


def simulate_motor(motor: MotorParameters) -> SimulationResults:
    """
    Perform a complete BLDC motor simulation.

    Parameters
    ----------
    motor : MotorParameters
        Motor input parameters.

    Returns
    -------
    SimulationResults
        Complete simulation results.
    """
    validate_motor_parameters(motor)

    electrical_power = calculate_electrical_power(
        motor.rated_voltage,
        motor.rated_current,
    )

    motor_rpm = calculate_motor_rpm(
        motor.kv_constant,
        motor.rated_voltage,
    )

    angular_velocity = calculate_angular_velocity(
        motor_rpm,
    )

    overall_efficiency = (
        motor.controller_efficiency
        * motor.motor_efficiency
    )

    mechanical_power = calculate_mechanical_power(
        electrical_power,
        overall_efficiency,
    )

    torque = calculate_torque(
        mechanical_power,
        angular_velocity,
    )

    wheel_rpm = calculate_wheel_rpm(
        motor_rpm,
        motor.gear_ratio,
    )

    vehicle_speed = calculate_vehicle_speed(
        wheel_rpm,
        motor.wheel_diameter,
    )

    wheel_force = calculate_wheel_force(
        torque,
        motor.wheel_diameter,
    )

    estimated_top_speed = calculate_estimated_top_speed(
        vehicle_speed,
    )

    return SimulationResults(
        electrical_power=electrical_power,
        mechanical_power=mechanical_power,
        motor_rpm=motor_rpm,
        wheel_rpm=wheel_rpm,
        angular_velocity=angular_velocity,
        torque=torque,
        wheel_force=wheel_force,
        vehicle_speed=vehicle_speed,
        estimated_top_speed=estimated_top_speed,
        overall_efficiency=overall_efficiency,
    )