MOTOR_PRESETS = {
    "250 W E-bike": {
        "rated_voltage": 36.0,
        "rated_current": 7.0,
        "kv_constant": 260.0,
        "pole_pairs": 15,
        "wheel_diameter": 0.66,
        "vehicle_mass": 100.0,
        "controller_efficiency": 0.92,
        "motor_efficiency": 0.88,
        "power": "250 W",
        "application": "Urban E-bike",
        "description": "Geared BLDC motor with 45:1 reduction."
    },

    "750 W E-bike": {
        "rated_voltage": 48.0,
        "rated_current": 18.0,
        "kv_constant": 300.0,
        "pole_pairs": 15,
        "wheel_diameter": 0.66,
        "vehicle_mass": 120.0,
        "controller_efficiency": 0.94,
        "motor_efficiency": 0.90,
        "power": "750 W",
        "application": "High-power E-bike",
        "description": "Geared BLDC motor with 35:1 reduction."
    },

    "1.5 kW Scooter": {
        "rated_voltage": 48.0,
        "rated_current": 30.0,
        "kv_constant": 320.0,
        "pole_pairs": 15,
        "wheel_diameter": 0.30,
        "vehicle_mass": 120.0,
        "controller_efficiency": 0.95,
        "motor_efficiency": 0.90,
        "power": "1.5 kW",
        "application": "Electric Scooter",
        "description": "Single-stage reduction drive."
    },

    "3 kW Motorcycle": {
        "rated_voltage": 72.0,
        "rated_current": 50.0,
        "kv_constant": 220.0,
        "pole_pairs": 20,
        "wheel_diameter": 0.43,
        "vehicle_mass": 180.0,
        "controller_efficiency": 0.96,
        "motor_efficiency": 0.93,
        "power": "3 kW",
        "application": "Electric Motorcycle",
        "description": "Chain-driven BLDC motor."
    },
}