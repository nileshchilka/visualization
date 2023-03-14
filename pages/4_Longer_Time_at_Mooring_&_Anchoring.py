import streamlit as st
from plot import percentage_of_vessels_which_took_longer_time_at_anchor, percentage_of_vessels_which_took_longer_time_at_mooring
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small


st.set_page_config(page_title="Longer Time at Mooring & Anchoring", page_icon="📈")
st.markdown(apmt_theme, unsafe_allow_html=True)
add_logo(apmt_logo_small, 10)

st.markdown("# Longer Time at Mooring & Anchoring")
st.sidebar.header("Longer Time at Mooring & Anchoring")

st.pyplot(fig=percentage_of_vessels_which_took_longer_time_at_mooring())

st.text("""Observations:
                Above graph depicts the Mooring pattern of the vessels which took more than 42 hours to moor for APMT & Non APMT terminals & Green line represents the Total Mooring time(APMT & Non APMT terminal).

                Formula:- for any given month, Total vessels which took more than 42 hours to moor/ Total vessels
                """)


st.pyplot(fig=percentage_of_vessels_which_took_longer_time_at_anchor())

st.text("""Observations:
            Above graph depicts the Anchoring pattern of the vessels which were anchored for more than 75 hours for APMT & Non APMT terminals & Green line represents the Total Anchring time(APMT & Non APMT terminal).

            Formula:- for any given month, vessels which took more than 75 hours to anchor/ Total vessels that anchored
            """)