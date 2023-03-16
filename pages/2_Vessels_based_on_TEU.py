import streamlit as st
from plot import per_of_vessels_based_on_teu
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small


st.set_page_config(page_title="Vessels based on TEU", page_icon="📈")
st.markdown(apmt_theme, unsafe_allow_html=True)
add_logo(apmt_logo_small, 10)

st.markdown("# Vessels based on TEU")
st.sidebar.header("Vessels based on TEU")

st.plotly_chart(per_of_vessels_based_on_teu(), use_container_width=True)

st.text("""Description:-
    • Above graph depicts the Percentage Distribution of the vessels based on
      Cargo Capacity on a monthly basis for APMT & Non APMT.
Observations:-
    • Non APMT serves more Smaller vessels than APMT
    • APMT serves more Larger vessels than Non APMT
Formula:- 
    • For any given month & terminal, count of each vessel category/Total count""")