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

st.image(add_img('images/apm-terminals-logo.png', 872, 239))

with st.sidebar:

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
            [data-testid="stSidebarNav"] {
            display: none;
            background-image: url(data:image/png;base64,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);
            background-repeat: no-repeat;
            padding-top: -30px;
            background-position: 20px 20px;
            }
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

