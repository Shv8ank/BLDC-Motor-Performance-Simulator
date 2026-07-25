from src.core.simulator import simulate_motor
from src.models.motor import MotorParameters


def test_complete_simulation():

    motor = MotorParameters(
        rated_voltage=48,
        rated_current=30,
        kv_constant=320,
        pole_pairs=15,
        wheel_diameter=0.30,
        vehicle_mass=120,
        gear_ratio=1.0,
        controller_efficiency=0.95,
        motor_efficiency=0.90,
    )

    results = simulate_motor(motor)

    assert results.electrical_power > 0
    assert results.mechanical_power > 0
    assert results.motor_rpm > 0
    assert results.wheel_rpm > 0
    assert results.angular_velocity > 0
    assert results.torque > 0
    assert results.vehicle_speed > 0
    assert results.wheel_force > 0
    assert results.estimated_top_speed > 0
    assert 0 < results.overall_efficiency <= 1