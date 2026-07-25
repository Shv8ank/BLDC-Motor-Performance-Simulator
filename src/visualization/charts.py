import numpy as np
import plotly.graph_objects as go


def generate_motor_curves(
    max_rpm: float,
    max_torque: float,
    base_speed_ratio: float = 0.60,
    points: int = 300,
):
    """
    Generate realistic BLDC motor characteristic curves.

    Returns:
        rpm, torque, power
    """

    rpm = np.linspace(1, max_rpm, points)

    base_rpm = max_rpm * base_speed_ratio

    base_omega = (2 * np.pi * base_rpm) / 60

    constant_power = max_torque * base_omega

    torque = np.zeros_like(rpm)
    power = np.zeros_like(rpm)

    for i, r in enumerate(rpm):

        omega = (2 * np.pi * r) / 60

        if r <= base_rpm:

            # Constant torque region
            torque[i] = max_torque

            # Power increases linearly with speed
            power[i] = max_torque * omega

        else:

            # Constant power region
            power[i] = constant_power

            # Torque decreases with speed
            torque[i] = constant_power / omega

    return rpm, torque, power


def create_torque_curve(
    max_rpm: float,
    max_torque: float,
    base_speed_ratio: float = 0.60,
):

    rpm, torque, _ = generate_motor_curves(
        max_rpm,
        max_torque,
        base_speed_ratio,
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
        x=max_rpm * base_speed_ratio,
        line_dash="dash",
        annotation_text="Base Speed",
    )

    fig.update_layout(
        title="BLDC Torque-Speed Characteristic",
        template="plotly_dark",
        height=450,
        xaxis_title="Motor RPM",
        yaxis_title="Torque (Nm)",
        hovermode="x unified",
    )

    return fig


def create_power_curve(
    max_rpm: float,
    max_torque: float,
    base_speed_ratio: float = 0.60,
):

    rpm, _, power = generate_motor_curves(
        max_rpm,
        max_torque,
        base_speed_ratio,
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
        x=max_rpm * base_speed_ratio,
        line_dash="dash",
        annotation_text="Base Speed",
    )

    fig.update_layout(
        title="BLDC Power-Speed Characteristic",
        template="plotly_dark",
        height=450,
        xaxis_title="Motor RPM",
        yaxis_title="Power (W)",
        hovermode="x unified",
    )

    return fig