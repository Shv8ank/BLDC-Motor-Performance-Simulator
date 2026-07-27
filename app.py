import streamlit as st


from src.models.motor import MotorParameters
from src.data.motors import MOTOR_PRESETS
from src.core.simulator import simulate_motor
from src.visualization.charts import (
    create_power_curve,
    create_torque_curve,
)
from src.core.vehicle_dynamics import *


st.set_page_config(
    page_title="BLDC Motor Performance Simulator",
    page_icon="⚡",
    layout="wide",
)

st.title("⚡ BLDC Motor Performance Simulator")
st.caption(
    "Interactive performance estimation for BLDC motors used in electric vehicles."
)

# ==========================
# Sidebar
# ==========================

st.sidebar.header("Motor Configuration")

selected_motor = st.sidebar.selectbox(
    "Motor Preset",
    list(MOTOR_PRESETS.keys()) + ["Custom"]
)

custom_edit = st.sidebar.checkbox(
    "Enable Custom Editing",
    value=(selected_motor == "Custom")
)

if selected_motor != "Custom":
    preset = MOTOR_PRESETS[selected_motor]
else:
    preset = {
        "rated_voltage": 36.0,
        "rated_current": 7.0,

        "rated_power": 250.0,

        "rated_speed": 260.0,
        "max_speed": 300.0,

        "rated_torque": 9.0,
        "peak_torque": 18.0,

        "wheel_diameter": 0.66,
        "vehicle_mass": 100.0,

        "controller_efficiency": 0.95,
        "motor_efficiency": 0.88,
    }    

rated_voltage = st.sidebar.number_input(
    "Rated Voltage (V)",
    value=preset["rated_voltage"],
    min_value=1.0,
    disabled=not custom_edit,
)

rated_current = st.sidebar.number_input(
    "Rated Current (A)",
    value=preset["rated_current"],
    min_value=0.1,
    disabled=not custom_edit,
)

rated_power = st.sidebar.number_input(
    "Rated Power (W)",
    value=preset["rated_power"],
    min_value=1.0,
    disabled=not custom_edit,
)

rated_speed = st.sidebar.number_input(
    "Rated Speed (RPM)",
    value=preset["rated_speed"],
    min_value=1.0,
    disabled=not custom_edit,
)

max_speed = st.sidebar.number_input(
    "Maximum Speed (RPM)",
    value=preset["max_speed"],
    min_value=1.0,
    disabled=not custom_edit,
)

rated_torque = st.sidebar.number_input(
    "Rated Torque (Nm)",
    value=preset["rated_torque"],
    min_value=0.1,
    disabled=not custom_edit,
)

peak_torque = st.sidebar.number_input(
    "Peak Torque (Nm)",
    value=preset["peak_torque"],
    min_value=0.1,
    disabled=not custom_edit,
)
wheel_diameter = st.sidebar.number_input(
    "Wheel Diameter (m)",
    value=preset["wheel_diameter"],
    min_value=0.05,
    disabled=not custom_edit,
)

vehicle_mass = st.sidebar.number_input(
    "Vehicle Mass (kg)",
    value=preset["vehicle_mass"],
    min_value=1.0,
    disabled=not custom_edit,
)

controller_efficiency = st.sidebar.slider(
    "Controller Efficiency",
    0.0,
    1.0,
    preset["controller_efficiency"],
    disabled=not custom_edit,
)

motor_efficiency = st.sidebar.slider(
    "Motor Efficiency",
    0.0,
    1.0,
    preset["motor_efficiency"],
    disabled=not custom_edit,
)

st.sidebar.subheader("Battery")

battery_voltage = st.sidebar.number_input(
    "Battery Voltage (V)",
    value=48.0,
)

battery_capacity = st.sidebar.number_input(
    "Battery Capacity (Ah)",
    value=20.0,
)

st.sidebar.subheader("Vehicle Dynamics")

drag_coefficient = st.sidebar.number_input(
    "Drag Coefficient (Cd)",
    value=0.60,
)

frontal_area = st.sidebar.number_input(
    "Frontal Area (m²)",
    value=0.70,
)

rolling_resistance = st.sidebar.number_input(
    "Rolling Resistance Coefficient",
    value=0.015,
)

road_angle = st.sidebar.slider(
    "Road Gradient (°)",
    0,
    20,
    0,
)

st.sidebar.divider()

run = st.sidebar.button(
    "▶ Run Simulation",
    use_container_width=True,
)

# ==========================
# Simulation
# ==========================

if run:

    try:

        motor = MotorParameters(
            rated_voltage=rated_voltage,
            rated_current=rated_current,

            rated_power=rated_power,

            rated_speed=rated_speed,
            max_speed=max_speed,

            rated_torque=rated_torque,
            peak_torque=peak_torque,

            wheel_diameter=wheel_diameter,
            vehicle_mass=vehicle_mass,

            controller_efficiency=controller_efficiency,
            motor_efficiency=motor_efficiency,
        )

        results = simulate_motor(motor)
        speed_mps = results.vehicle_speed / 3.6
        rolling_force = rolling_resistance_force(
            vehicle_mass,
            rolling_resistance,
        )

        drag_force = aerodynamic_drag_force(
            speed_mps,
            drag_coefficient,
            frontal_area,
        )

        grade_force = grade_resistance_force(
            vehicle_mass,
            road_angle,
        )

        available_force = net_force(
            results.wheel_force,
            rolling_force,
            drag_force,
            grade_force,
        )

        vehicle_acceleration = acceleration(
            available_force,
            vehicle_mass,
        )

        estimated_top_speed = estimate_top_speed(
            results.wheel_force,
            drag_coefficient,
            frontal_area,
        )

        power_weight = (
            results.mechanical_power
            / vehicle_mass
        )

        # ==========================
        # Metrics
        # ==========================

        row1 = st.columns(4)

        row1[0].metric(
            "⚡ Electrical Power",
            f"{results.electrical_power:.2f} W",
        )

        row1[1].metric(
            "🔄 Motor RPM",
            f"{results.motor_rpm:.0f}",
        )

        row1[2].metric(
            "🌀 Torque",
            f"{results.torque:.2f} Nm",
        )

        row2 = st.columns(4)

        row2[0].metric(
             "🚗 Wheel RPM",
            f"{results.wheel_rpm:.0f}",
        )

        row2[1].metric(
            "🚙 Vehicle Speed",
            f"{results.vehicle_speed:.2f} km/h",
        )

        row2[2].metric(
            "⚙️ Wheel Force",
            f"{results.wheel_force:.2f} N",
        )

        row2[3].metric(
            "✅ Overall Efficiency",
            f"{results.overall_efficiency * 100:.1f} %",
        )

        st.info(
            "Vehicle speed is the theoretical no-load speed calculated from hub motor RPM and wheel diameter. "
            "Actual road speed is lower due to aerodynamic drag, rolling resistance, road gradient, controller limits and load."
        )

        st.divider()

        # ==========================
        # Charts
        # ==========================

        power_chart = create_power_curve(
            motor.rated_speed,
            motor.max_speed,
            motor.rated_torque,
            motor.peak_torque,
        )

        torque_chart = create_torque_curve(
            motor.rated_speed,
            motor.max_speed,
            motor.rated_torque,
            motor.peak_torque,
        )

        graph1, graph2 = st.columns(2)

        with graph1:
            st.plotly_chart(
                power_chart,
                use_container_width=True,
            )

        with graph2:
            st.plotly_chart(
                torque_chart,
                use_container_width=True,
            )

        st.divider()

        if selected_motor != "Custom":

            st.subheader("Motor Information")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Power Rating:** {preset['power']}")
                st.write(f"**Application:** {preset['application']}")

            with col2:
                st.write("**Description:**")
                st.write(preset["description"])

        st.divider()

        st.subheader("🚗 Vehicle Dynamics")

        left, right = st.columns(2)

        with left:

            st.metric(
                "Power-to-Weight",
                f"{power_weight:.2f} W/kg",
            )

            st.metric(
                "Net Tractive Force",
                f"{available_force:.2f} N",
            )

            st.metric(
                "Acceleration",
                f"{vehicle_acceleration:.2f} m/s²",
            )

        with right:

            st.metric(
                "Rolling Resistance",
                f"{rolling_force:.2f} N",
            )

            st.metric(
                "Aerodynamic Drag",
                f"{drag_force:.2f} N",
            )

            st.metric(
                "Estimated Top Speed",
                f"{estimated_top_speed:.2f} km/h",
            )
    except Exception as e:
        st.error(str(e))
