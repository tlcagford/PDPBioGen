import streamlit as st
import numpy as np

def render_dashboard(states):
    st.title("Multimodal Closed-Loop Simulation Dashboard")

    st.line_chart(states[:, -2], height=200)
    st.write("Neural Fusion Output")

    st.line_chart(states[:, -1], height=200)
    st.write("Controller Output")

    st.line_chart(states[:, 2], height=200)
    st.write("Heart Rate")

    st.line_chart(states[:, 4], height=200)
    st.write("Glucose")
