import math

# Physical constants
GRAVITY = 9.81          # m/s²
AIR_DENSITY = 1.225     # kg/m³


def rolling_resistance_force(
    mass: float,
    rolling_coefficient: float = 0.015,
):
    """
    Rolling resistance force (N)
    """
    return rolling_coefficient * mass * GRAVITY


def aerodynamic_drag_force(
    speed_mps: float,
    drag_coefficient: float = 0.60,
    frontal_area: float = 0.70,
):
    """
    Aerodynamic drag force (N)
    """
    return (
        0.5
        * AIR_DENSITY
        * drag_coefficient
        * frontal_area
        * speed_mps ** 2
    )


def grade_resistance_force(
    mass: float,
    road_angle_deg: float,
):
    """
    Hill climbing resistance (N)
    """
    angle = math.radians(road_angle_deg)

    return mass * GRAVITY * math.sin(angle)


def net_force(
    tractive_force: float,
    rolling_force: float,
    drag_force: float,
    grade_force: float,
):
    """
    Remaining force available for acceleration.
    """
    return (
        tractive_force
        - rolling_force
        - drag_force
        - grade_force
    )


def acceleration(
    net_force_value: float,
    mass: float,
):
    """
    Vehicle acceleration (m/s²)
    """
    return max(0.0, net_force_value / mass)


def estimate_top_speed(
    wheel_force: float,
    drag_coefficient: float = 0.60,
    frontal_area: float = 0.70,
):
    """
    Estimate top speed where drag balances wheel force.
    """

    speed = math.sqrt(
        (2 * wheel_force)
        / (
            AIR_DENSITY
            * drag_coefficient
            * frontal_area
        )
    )

    return speed * 3.6