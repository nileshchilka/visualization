import streamlit as st
from plot import mooring_duration_distribution, anchor_duration_distribution
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small


st.set_page_config(page_title="Mooring & Anchoring Distribution", page_icon="📈")
st.markdown(apmt_theme, unsafe_allow_html=True)
add_logo(apmt_logo_small, 10)

st.markdown("# Mooring & Anchoring Distribution")
st.sidebar.header("Mooring & Anchoring Distribution")

st.pyplot(fig=mooring_duration_distribution())

st.text("""Observations:
            Above graph shows the mooring distribution on Hourly basis for both APMT & Non APMT Terminals.

            Formula: -  for any given month, count of each vessel category/ Total vessels

            """)

st.pyplot(fig=anchor_duration_distribution())

st.text("""Observations:
            Above graph shows the Anchor distribution on Hourly basis for both APMT & Non APMT Terminals.

            Formula: -  for any given month, count of each vessel category that anchored/ Total vessels that anchored
            """)


