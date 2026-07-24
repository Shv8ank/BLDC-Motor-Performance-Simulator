from src.models.motor import MotorParameters


motor = MotorParameters(
    rated_voltage=48,
    rated_current=30,
    kv_constant=320,
    pole_pairs=15,
    wheel_diameter=0.45,
    vehicle_mass=160,
)

print(motor)