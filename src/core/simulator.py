"""
Simulation engine for the EV Hub Motor Performance Simulator.
"""

from src.models.motor import MotorParameters
from src.models.results import SimulationResults

from src.core.validators import validate_motor_parameters

from src.core.calculations import (
    calculate_angular_velocity,
    calculate_electrical_power,
    calculate_mechanical_power,
    calculate_motor_rpm,
    calculate_torque,
    calculate_vehicle_speed,
    calculate_wheel_force,
)


def simulate_motor(
    motor: MotorParameters,
) -> SimulationResults:
    """
    Perform a complete hub motor simulation.

    Parameters
    ----------
    motor : MotorParameters
        Input motor parameters.

    Returns
    -------
    SimulationResults
        Complete simulation results.
    """

    # ------------------------------------------
    # Validate Inputs
    # ------------------------------------------

    validate_motor_parameters(motor)

    # ------------------------------------------
    # Electrical Model
    # ------------------------------------------

    electrical_power = calculate_electrical_power(
        motor.rated_voltage,
        motor.rated_current,
    )

    overall_efficiency = (
        motor.controller_efficiency
        * motor.motor_efficiency
    )

    mechanical_power = motor.rated_power * motor.motor_efficiency

    # ------------------------------------------
    # Hub Motor Model
    # ------------------------------------------

    motor_rpm = motor.rated_speed

    angular_velocity = calculate_angular_velocity(
        motor_rpm,
    )

    motor_torque = motor.rated_torque

    # ------------------------------------------
    # Wheel Model
    # (Direct-drive hub motor)
    # ------------------------------------------

    wheel_rpm = motor_rpm

    wheel_force = calculate_wheel_force(
        motor_torque,
        motor.wheel_diameter,
    )

    vehicle_speed = calculate_vehicle_speed(
        wheel_rpm,
        motor.wheel_diameter,
    )

    # ------------------------------------------
    # Results
    # ------------------------------------------

    return SimulationResults(
        electrical_power=electrical_power,
        mechanical_power=mechanical_power,

        motor_rpm=motor_rpm,
        wheel_rpm=wheel_rpm,
        angular_velocity=angular_velocity,

        torque=motor_torque,
        wheel_force=wheel_force,

        vehicle_speed=vehicle_speed,
        estimated_top_speed=vehicle_speed,

        overall_efficiency=overall_efficiency,
    )