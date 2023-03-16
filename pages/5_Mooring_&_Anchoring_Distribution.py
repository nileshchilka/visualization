import streamlit as st
from plot import mooring_duration_distribution, anchor_duration_distribution
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small


st.set_page_config(page_title="Mooring & Anchoring Distribution", page_icon="📈")
st.markdown(apmt_theme, unsafe_allow_html=True)
add_logo(apmt_logo_small, 10)

st.markdown("# Mooring & Anchoring Distribution")
st.sidebar.header("Mooring & Anchoring Distribution")

st.plotly_chart(mooring_duration_distribution(), use_container_width=True)

st.text("""Description:-
    • Above graph shows the mooring distribution on Hourly basis for both APMT & 
    Non APMT Terminals.
Observations:-
    • APMT has performed better than Non APMT in range of 0-10 in hrs
    • Non APMT has performed better than APMT in below 30 hrs
Formula:-  
    • for any given month, count of each vessel category/ Total vessels

            """)

st.plotly_chart(anchor_duration_distribution(), use_container_width=True)

st.text("""Description:-
    • Above graph shows the Anchor distribution on Hourly basis for both APMT & 
      Non APMT Terminals.
Observations:-
    • Non APMT has performed better than APMT in range of 0-10 in hrs
    • Non APMT has performed better than APMT in below 30 hrs
    • Percentage of 70+ hrs is more in APMT than Non APMT but APMT outperformed 
      in January with no vessels taking more time than 50 hrs
Formula:-  
    • for any given month, count of each vessel category that anchored/ Total 
      vessels that anchored
            """)


