import numpy as np
import plotly.graph_objects as go


def generate_motor_curves(
    rated_speed: float,
    max_speed: float,
    rated_torque: float,
    peak_torque: float,
    points: int = 300,
):
    """
    Generate realistic EV hub motor torque-speed and power-speed curves.

    Regions:
    1. Constant peak torque
    2. Torque tapers to rated torque
    3. Constant power
    """

    rpm = np.linspace(0, max_speed, points)

    torque = np.zeros_like(rpm)
    power = np.zeros_like(rpm)

    transition_speed = rated_speed * 0.5

    rated_omega = (2 * np.pi * rated_speed) / 60
    constant_power = rated_torque * rated_omega

    for i, r in enumerate(rpm):

        omega = (2 * np.pi * r) / 60

        if r <= transition_speed:

            # Peak torque region
            torque[i] = peak_torque

        elif r <= rated_speed:

            # Smooth transition from peak torque to rated torque
            ratio = (r - transition_speed) / (rated_speed - transition_speed)

            torque[i] = (
                peak_torque
                - ratio * (peak_torque - rated_torque)
            )

        else:

            # Constant power region
            if omega > 0:
                torque[i] = constant_power / omega
            else:
                torque[i] = rated_torque

        power[i] = torque[i] * omega

    return rpm, torque, power


def create_torque_curve(
    rated_speed: float,
    max_speed: float,
    rated_torque: float,
    peak_torque: float,
):

    rpm, torque, _ = generate_motor_curves(
        rated_speed,
        max_speed,
        rated_torque,
        peak_torque,
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=rpm,
            y=torque,
            mode="lines",
            name="Torque",
            line=dict(width=4),
        )
    )

    fig.add_vline(
        x=rated_speed,
        line_dash="dash",
        annotation_text="Rated Speed",
    )

    fig.add_vline(
        x=max_speed,
        line_dash="dot",
        annotation_text="Maximum Speed",
    )

    fig.update_layout(
        title="Motor Torque-Speed Characteristic",
        template="plotly_dark",
        height=450,
        xaxis_title="Motor Speed (RPM)",
        yaxis_title="Torque (Nm)",
        hovermode="x unified",
    )

    return fig


def create_power_curve(
    rated_speed: float,
    max_speed: float,
    rated_torque: float,
    peak_torque: float,
):

    rpm, _, power = generate_motor_curves(
        rated_speed,
        max_speed,
        rated_torque,
        peak_torque,
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=rpm,
            y=power,
            mode="lines",
            name="Power",
            line=dict(width=4),
        )
    )

    fig.add_vline(
        x=rated_speed,
        line_dash="dash",
        annotation_text="Rated Speed",
    )

    fig.add_vline(
        x=max_speed,
        line_dash="dot",
        annotation_text="Maximum Speed",
    )

    fig.update_layout(
        title="Motor Power-Speed Characteristic",
        template="plotly_dark",
        height=450,
        xaxis_title="Motor Speed (RPM)",
        yaxis_title="Power (W)",
        hovermode="x unified",
    )

    return fig