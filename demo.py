import pandas as pd

import streamlit as st

st.markdown(
    """
    <style>
    h1 {
        color: red;
    }

    [data-testid="stVerticalBlock"] > div:nth-last-child(2) [data-testid="stExpander"] details summary,
    [data-testid="stVerticalBlock"] > div:nth-last-child(2) [data-testid="stExpander"] details[open] summary {
        background-color: #1f77ff;
        color: white;
    }

    [data-testid="stVerticalBlock"] > div:nth-last-child(2) [data-testid="stExpander"] [data-testid="stMarkdownContainer"] p {
        color: brown;
    }

    [data-testid="stVerticalBlock"] > div:nth-last-child(1) [data-testid="stExpander"] details summary {
        background-color: #2ca02c;
        color: white;
    }

    [data-testid="stVerticalBlock"] > div:nth-last-child(1) [data-testid="stExpander"] details[open] summary {
        background-color: #ffd700;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Expander Test")

with st.expander("Click ME!"):
    st.write("This is content")
    st.button("A button", key="first_expander_button")

with st.expander("Another one"):
    st.write("More content here")