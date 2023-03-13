import streamlit as st
from plot import per_of_vessels_based_on_teu

st.set_page_config(page_title="Vessels based on TEU", page_icon="📈")

st.markdown("# Vessels based on TEU")
st.sidebar.header("Vessels based on TEU")

st.pyplot(fig=per_of_vessels_based_on_teu())

st.text("""Observations:
            Above graph depicts the Percentage Distribution of the vessels based on Cargo Capacity on a monthly basis for APMT & Non APMT.

            Formula:- For any given month, count of each vessel category/ Total count""")