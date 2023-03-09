import streamlit as st
import numpy as np
# import plotly.graph_objects as go

from plot import *

st.pyplot(fig=vessel_dis_per())

st.pyplot(fig=vessel_distribution_count())

st.pyplot(fig=per_of_vessels_based_on_teu())

st.pyplot(fig=percentage_of_vessels_not_anchored_before_serving())

st.pyplot(fig=percentage_of_vessels_anchored_before_serving())

st.pyplot(fig=percentage_of_vessels_which_took_longer_time_at_mooring())

st.pyplot(fig=percentage_of_vessels_which_took_longer_time_at_anchor())

st.pyplot(fig=percentage_vessels_not_anchored_before_serving_line())

st.pyplot(fig=anchor_duration_distribution())

st.pyplot(fig=mooring_duration_distribution())

st.pyplot(fig=shipping_line_analysis())

st.pyplot(fig=top_6_APMT_vs_Non_APMT_Terminals_on_port_stay())

st.pyplot(fig=top_6_APMT_vs_Non_APMT_Terminals_on_port_traffic())

















