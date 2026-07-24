import streamlit as st

st.set_page_config(
    page_title="BLDC Motor Performance Simulator",
    page_icon="⚡",
    layout="wide",
)

st.title("⚡ BLDC Motor Performance Simulator")

st.markdown(
    """
    Welcome to the BLDC Motor Performance Simulator.

    This application will calculate and visualize key motor performance
    characteristics including torque, power, efficiency, RPM, and vehicle speed.
    """
)

st.info("Milestone 1: Project initialized successfully.")