import streamlit as st
from plot import vessel_dis_per, vessel_distribution_count
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small

st.set_page_config(page_title="Vessel Distribution", page_icon="📈")
st.markdown(apmt_theme, unsafe_allow_html=True)
add_logo(apmt_logo_small, 10)

st.markdown("# Vessel Distribution")
st.sidebar.header("Vessel Distribution")

st.plotly_chart(vessel_dis_per(), use_container_width=True, sharing="streamlit", theme="streamlit")

st.text("""Observations:
            Above plot depicts Vessel distribution Per Terminal on the basis of cargo capacity.
            X-axis represents two APMT terminals of Rotterdam & Top 3 Non-APMT terminals.
            For both APMT & Non APMT terminals majority of the vessels fall in the category of 250-1000 & 1000-4000 TEUs cargo capacity.

            Formula:- For any given terminal, count of each vessel category/ Total count
            """)


st.plotly_chart(vessel_distribution_count(), use_container_width=True, sharing="streamlit", theme="streamlit")

st.text("""Observations:
            This plot depicts Vessel count distribution per terminal of the Rotterdam port on the basis of Cargo capacity for the 7 months data.
            We observe that out of all terminals ECT Delta(a Non APMT terminal) has the highest distinct count of the vessel visits(Not Distinct IMO). followed by Rotterdam Short sea terminal & Rotterdam world gateway.
            APMT terminals have relatively lower Vessel visits and most of these vessels fall in the 250-1000 & 1000-4000 TEUs category.

            Formula:- For any given terminal, count of each vessel category
            """)
