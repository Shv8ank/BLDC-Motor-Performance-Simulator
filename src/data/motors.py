MOTOR_PRESETS = {
    "250 W E-bike": {
        "rated_voltage": 36.0,
        "rated_current": 7.0,
        "rated_power": 250.0,

        "rated_speed": 260.0,
        "max_speed": 300.0,

        "rated_torque": 9.0,
        "peak_torque": 18.0,

        "wheel_diameter": 0.66,
        "vehicle_mass": 100.0,

        "battery_voltage": 36.0,
        "battery_capacity": 10.0,

        "controller_efficiency": 0.95,
        "motor_efficiency": 0.88,

        "power": "250 W",
        "application": "Urban E-bike",
        "description": "Direct-drive BLDC hub motor for city commuting.",
    },

    "750 W E-bike": {
        "rated_voltage": 48.0,
        "rated_current": 16.0,
        "rated_power": 750.0,

        "rated_speed": 340.0,
        "max_speed": 380.0,

        "rated_torque": 22.0,
        "peak_torque": 40.0,

        "wheel_diameter": 0.70,
        "vehicle_mass": 120.0,

        "battery_voltage": 48.0,
        "battery_capacity": 15.0,

        "controller_efficiency": 0.95,
        "motor_efficiency": 0.90,

        "power": "750 W",
        "application": "Performance E-bike",
        "description": "High-torque direct-drive hub motor for trekking and cargo bikes.",
    },

    "1.5 kW Scooter": {
        "rated_voltage": 60.0,
        "rated_current": 30.0,
        "rated_power": 1500.0,

        "rated_speed": 500.0,
        "max_speed": 600.0,

        "rated_torque": 38.0,
        "peak_torque": 70.0,

        "wheel_diameter": 0.48,
        "vehicle_mass": 150.0,

        "battery_voltage": 60.0,
        "battery_capacity": 25.0,

        "controller_efficiency": 0.96,
        "motor_efficiency": 0.91,

        "power": "1.5 kW",
        "application": "Electric Scooter",
        "description": "Direct-drive hub motor for urban electric scooters.",
    },

    "3 kW Motorcycle": {
        "rated_voltage": 72.0,
        "rated_current": 50.0,
        "rated_power": 3000.0,

        "rated_speed": 850.0,
        "max_speed": 1000.0,

        "rated_torque": 60.0,
        "peak_torque": 110.0,

        "wheel_diameter": 0.60,
        "vehicle_mass": 220.0,

        "battery_voltage": 72.0,
        "battery_capacity": 40.0,

        "controller_efficiency": 0.97,
        "motor_efficiency": 0.93,

        "power": "3 kW",
        "application": "Electric Motorcycle",
        "description": "High-performance BLDC hub motor for lightweight electric motorcycles.",
    },
}