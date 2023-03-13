from msal_streamlit_authentication import msal_authentication

import streamlit as st
import os

st.set_page_config(
    page_title="EDA",
    layout="wide"
)
if os.environ["env"] == "dev":
    os.environ["redirect_uri"] = "http://localhost:8501/"
else:
    os.environ["redirect_uri"] = "https://nileshchilka-visualization-eda-urmkkl.streamlit.app/"

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
        print("inside")

        st.write("# EDA - APMT v/s Non APMT! ")

        st.sidebar.success("Select a plot above.")

        st.markdown(
            """
            Some info.
        """
        )
else:
    no_sidebar_style = """
        <style>
            section[data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
