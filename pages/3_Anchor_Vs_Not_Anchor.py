import streamlit as st
from plot import percentage_of_vessels_not_anchored_before_serving, \
    percentage_of_vessels_anchored_before_serving, percentage_vessels_not_anchored_before_serving_line

st.set_page_config(page_title="Anchor Vs Not Anchor", page_icon="📈")

st.markdown("# Anchor Vs Not Anchor")
st.sidebar.header("Anchor Vs Not Anchor")

st.pyplot(fig=percentage_of_vessels_not_anchored_before_serving())

st.text("""Observations:
            This plot depicts the vessel anchoring pattern on a monthly basis, Vessels which had zero waiting time.
            X-axis shows months & Y-axis shows Percentage of the vessel visits.
            APMT has performed slightly better overall compared to Non APMT terminals.

            Formula :- for any given month, Total vessels not anchored/ Total vessels """)

st.pyplot(fig=percentage_of_vessels_anchored_before_serving())

st.text("""Observations:
            This plot depicts the Anchoring behavior of the APMT & Non APMT terminals on a monthly basis.
            From this graph we observe that APMT has lower waiting time for the vessels compared to Non APMT terminals.

            Formula:- for any given month, Total vessels anchored/ Total vessels """)

st.pyplot(fig=percentage_vessels_not_anchored_before_serving_line())

st.text("""Observations:
            Above graph shows the Percentage of the vessels which were served instantly(Zero Waiting Time).
            We see that APMT has outperformed Non APMT terminals and has zero waiting time for the vessels.

            Formula :- for any given month, Total vessels not anchored/ Total vessels""")