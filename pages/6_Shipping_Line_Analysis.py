import streamlit as st
from plot import shipping_line_analysis

st.set_page_config(page_title="Shipping Line Analysis", page_icon="📈")

st.markdown("# Shipping Line Analysis")
st.sidebar.header("Shipping Line Analysis")

st.pyplot(fig=shipping_line_analysis())

st.text("""Observations:
            Shows the distribution of the Shipping lines per terminal for 7 months period

            Formula:- For any given APMT or Non APMT terminal, count of vessels of particular shipping line / total count of vessels
            """)