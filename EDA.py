from msal_streamlit_authentication import msal_authentication
from streamlit_extras.app_logo import add_logo
from constants import apmt_theme, apmt_logo_small
from utils import add_img

import streamlit as st
import os

st.set_page_config(page_title="EDA", layout="wide")

add_logo(apmt_logo_small, 10)

st.markdown(apmt_theme, unsafe_allow_html=True)

if os.environ["env"] == "dev":
    os.environ["redirect_uri"] = "http://localhost:8501/"
else:
    os.environ["redirect_uri"] = "https://visualization-eda-dev.streamlit.app/"


col1, col2 = st.columns([3, 1])

with col1:

    st.image(add_img('images/apm-terminals-logo.png', 872, 239))

with col2:
    login_token = msal_authentication(
    auth={
        "clientId": os.environ["client-id"],
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

        st.write("# EDA - APMT v/s Non APMT! ")

        st.sidebar.success("Select a plot above.")

        st.markdown(
            """
            Note:- 

1. Period under consideration July-2022 till January-2023
2. Geo distance of 80 KM is considered for analysis
3. Median is considered for comparison as mean is detrimental to outliers

        """
        )
else:
    no_sidebar_style = """
        <style>
            section[data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
