import streamlit as st
from plot import shipping_line_analysis
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small


st.set_page_config(page_title="Shipping Line Analysis", page_icon="📈")
st.markdown(apmt_theme, unsafe_allow_html=True)
add_logo(apmt_logo_small, 10)

st.markdown("# Shipping Line Analysis")
st.sidebar.header("Shipping Line Analysis")

st.plotly_chart(shipping_line_analysis(), use_container_width=True)

st.text("""Description:-
    • Shows the distribution of the Shipping lines for 7 months period
Observations:-
    • Non APMT serves more vessels of Unifeeder, X-Press Feeders &
      Samskip North Atlantic Logistics
    • APMT serves more vessels of BG Freight Line and Maersk Line
    • APMT has monopoly of Maersk Line 
    • Non APMT has monopoly of Samskip North Atlantic Logistics
Formula:- 
    • For any given APMT or Non APMT terminal, count of vessels of particular 
      shipping line / total count of vessels
            """)