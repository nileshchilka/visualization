import streamlit as st
from plot import top_6_APMT_vs_Non_APMT_Terminals_on_port_traffic, top_6_APMT_vs_Non_APMT_Terminals_on_port_stay
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small


st.set_page_config(page_title="Port Stay & Port Traffic", page_icon="📈")
st.markdown(apmt_theme, unsafe_allow_html=True)
add_logo(apmt_logo_small, 10)

st.markdown("# Port Stay & Port Traffic")
st.sidebar.header("Port Stay & Port Traffic")

st.plotly_chart(top_6_APMT_vs_Non_APMT_Terminals_on_port_stay(), use_container_width=True)

st.text("""Observations:
    Shows Median Port Stay Duration of Top 6 terminals of APMT vs Top 6 terminals 
    of Non APMT
    We see that Non APMT has outperformed APMT terminals having less port stay time.
    """)


st.plotly_chart(top_6_APMT_vs_Non_APMT_Terminals_on_port_traffic(), use_container_width=True)

st.text("""Observations:
    Shows the count of vessels served on daily basis at Top 6 terminals of APMT vs 
    Top 6 terminals of Non APMT
    We see that Non APMT has outperformed APMT terminals while serving more vessels 
    on daily basis
    """)