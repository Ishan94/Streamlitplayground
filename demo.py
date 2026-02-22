import pandas as pd

import streamlit as st
st.title("Expander Test")

with st.expander("Click ME!"):
    st.write("This is content")
    st.button("A button")

with st.expander("Another one"):
    st.write("More content here")