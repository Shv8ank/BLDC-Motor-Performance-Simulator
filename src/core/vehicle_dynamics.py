"""
Vehicle dynamics calculations for the EV Performance Simulator.
"""

import math

# ==========================================================
# Physical Constants
# ==========================================================

GRAVITY = 9.81          # m/s²
AIR_DENSITY = 1.225     # kg/m³


# ==========================================================
# Rolling Resistance
# ==========================================================

def rolling_resistance_force(
    mass: float,
    rolling_coefficient: float = 0.012,
) -> float:
    """
    Calculates rolling resistance force.

    Parameters
    ----------
    mass : float
        Vehicle mass (kg)

    rolling_coefficient : float
        Rolling resistance coefficient
        Typical values:
            Road bike      : 0.003–0.006
            E-bike         : 0.005–0.010
            Scooter        : 0.010–0.015
            Motorcycle     : 0.012–0.018

    Returns
    -------
    float
        Rolling resistance force (N)
    """

    return rolling_coefficient * mass * GRAVITY


# ==========================================================
# Aerodynamic Drag
# ==========================================================

def aerodynamic_drag_force(
    speed_mps: float,
    drag_coefficient: float = 0.50,
    frontal_area: float = 0.60,
) -> float:
    """
    Calculates aerodynamic drag force.

    Parameters
    ----------
    speed_mps : float
        Vehicle speed (m/s)

    drag_coefficient : float
        Aerodynamic drag coefficient (Cd)

    frontal_area : float
        Vehicle frontal area (m²)

    Returns
    -------
    float
        Drag force (N)
    """

    return (
        0.5
        * AIR_DENSITY
        * drag_coefficient
        * frontal_area
        * speed_mps ** 2
    )


# ==========================================================
# Grade Resistance
# ==========================================================

def grade_resistance_force(
    mass: float,
    road_angle_deg: float,
) -> float:
    """
    Calculates hill-climbing resistance.

    Parameters
    ----------
    mass : float
        Vehicle mass (kg)

    road_angle_deg : float
        Road incline (degrees)

    Returns
    -------
    float
        Grade resistance force (N)
    """

    angle = math.radians(road_angle_deg)

    return mass * GRAVITY * math.sin(angle)


# ==========================================================
# Net Tractive Force
# ==========================================================

def net_force(
    tractive_force: float,
    rolling_force: float,
    drag_force: float,
    grade_force: float,
) -> float:
    """
    Calculates the remaining force available for acceleration.
    """

    return max(
        0.0,
        tractive_force
        - rolling_force
        - drag_force
        - grade_force,
    )


# ==========================================================
# Vehicle Acceleration
# ==========================================================

def acceleration(
    net_force_value: float,
    mass: float,
) -> float:
    """
    Calculates vehicle acceleration.

    Returns
    -------
    float
        Acceleration (m/s²)
    """

    if mass <= 0:
        return 0.0

    return net_force_value / mass


# ==========================================================
# Estimated Top Speed
# ==========================================================

def estimate_top_speed(
    wheel_force: float,
    drag_coefficient: float = 0.50,
    frontal_area: float = 0.60,
) -> float:
    """
    Estimates aerodynamic-limited top speed.

    This ignores motor RPM limits and assumes the available
    wheel force is balanced only by aerodynamic drag.

    Returns
    -------
    float
        Estimated top speed (km/h)
    """

    if wheel_force <= 0:
        return 0.0

    speed = math.sqrt(
        (
            2 * wheel_force
        ) / (
            AIR_DENSITY
            * drag_coefficient
            * frontal_area
        )
    )

    return speed * 3.6