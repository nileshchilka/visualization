import os

from msal_streamlit_authentication import msal_authentication
from plot import *

import streamlit as st
# import plotly.graph_objects as go

st.set_page_config(layout="wide")

if os.environ["env"]:
    os.environ["redirect_uri"] = "http://localhost:8501/"
else:
    os.environ["redirect_uri"] = "http://localhost:8501/"

login_token = msal_authentication(
    auth={
        "clientId": os.environ["client_id"],
        "authority": os.environ["authority"],
        "redirectUri": os.environ["redirect_uri"],
        "postLogoutRedirectUri": "/"
    }, # Corresponds to the 'auth' configuration for an MSAL Instance
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    }, # Corresponds to the 'cache' configuration for an MSAL Instance
    login_request={
        "scopes": [os.environ["scopes"]]
    }, # Optional
    logout_request={}, # Optional
    login_button_text="Login", # Optional, defaults to "Login"
    logout_button_text="Logout", # Optional, defaults to "Logout"
    key=1 # Optional if only a single instance is needed
)

if login_token is not None:

    if "accessToken" in login_token.keys():
        print("inside")
        st.header("AIS EDA")

        col1, col2 = st.columns(2)

        with col1:

            st.pyplot(fig=vessel_dis_per())

            st.text("""Observations:
                Above plot depicts Vessel distribution Per Terminal on the basis of cargo capacity.
                X-axis represents two APMT terminals of Rotterdam & Top 3 Non-APMT terminals.
                For both APMT & Non APMT terminals majority of the vessels fall in the category of 250-1000 & 1000-4000 TEUs cargo capacity.
    
                Formula:- For any given terminal, count of each vessel category/ Total count
                """)

        with col2:

            st.pyplot(fig=vessel_distribution_count())

            st.text("""Observations:
                This plot depicts Vessel count distribution per terminal of the Rotterdam port on the basis of Cargo capacity for the 7 months data.
                We observe that out of all terminals ECT Delta(a Non APMT terminal) has the highest distinct count of the vessel visits(Not Distinct IMO). followed by Rotterdam Short sea terminal & Rotterdam world gateway.
                APMT terminals have relatively lower Vessel visits and most of these vessels fall in the 250-1000 & 1000-4000 TEUs category.
    
                Formula:- For any given terminal, count of each vessel category
                """)

        st.pyplot(fig=per_of_vessels_based_on_teu())

        st.text("""Observations:
            Above graph depicts the Percentage Distribution of the vessels based on Cargo Capacity on a monthly basis for APMT & Non APMT.
    
            Formula:- For any given month, count of each vessel category/ Total count""")

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

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig=percentage_of_vessels_which_took_longer_time_at_mooring())

            st.text("""Observations:
                Above graph depicts the Mooring pattern of the vessels which took more than 42 hours to moor for APMT & Non APMT terminals & Green line represents the Total Mooring time(APMT & Non APMT terminal).
    
                Formula:- for any given month, Total vessels which took more than 42 hours to moor/ Total vessels
                """)

        with col2:
            st.pyplot(fig=percentage_of_vessels_which_took_longer_time_at_anchor())

            st.text("""Observations:
                Above graph depicts the Anchoring pattern of the vessels which were anchored for more than 75 hours for APMT & Non APMT terminals & Green line represents the Total Anchring time(APMT & Non APMT terminal).
    
                Formula:- for any given month, vessels which took more than 75 hours to anchor/ Total vessels that anchored
                """)

        st.pyplot(fig=percentage_vessels_not_anchored_before_serving_line())

        st.text("""Observations:
            Above graph shows the Percentage of the vessels which were served instantly(Zero Waiting Time).
            We see that APMT has outperformed Non APMT terminals and has zero waiting time for the vessels.
    
            Formula :- for any given month, Total vessels not anchored/ Total vessels""")

        st.pyplot(fig=anchor_duration_distribution())

        st.text("""Observations:
            Above graph shows the Anchor distribution on Hourly basis for both APMT & Non APMT Terminals.
    
            Formula: -  for any given month, count of each vessel category that anchored/ Total vessels that anchored
            """)

        st.pyplot(fig=mooring_duration_distribution())

        st.text("""Observations:
            Above graph shows the mooring distribution on Hourly basis for both APMT & Non APMT Terminals.
    
            Formula: -  for any given month, count of each vessel category/ Total vessels
    
            """)

        st.pyplot(fig=shipping_line_analysis())

        st.text("""Observations:
            Shows the distribution of the Shipping lines per terminal for 7 months period
    
            Formula:- For any given APMT or Non APMT terminal, count of vessels of particular shipping line / total count of vessels
            """)

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig=top_6_APMT_vs_Non_APMT_Terminals_on_port_stay())

            st.text("""Observations:
                Shows Median Port Stay Duration of Top 6 terminals of APMT vs Top 6 terminals of Non APMT
                We see that Non APMT has outperformed APMT terminals having less port stay time.
                """)

        with col2:
            st.pyplot(fig=top_6_APMT_vs_Non_APMT_Terminals_on_port_traffic())

            st.text("""Observations:
                Shows the count of vessels served on daily basis at Top 6 terminals of APMT vs Top 6 terminals of Non APMT
                We see that Non APMT has outperformed APMT terminals while serving more vessels on daily basis
                """)

    else:
        st.write("Failed to Login")

















