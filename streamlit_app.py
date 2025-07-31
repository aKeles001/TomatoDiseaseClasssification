import streamlit as st

home = st.Page("home.py", title="Home Page")
tomato = st.Page("tomato.py", title="Tomato Leaf Disease")
apple = st.Page("apple.py", title="Apple Leaf Disease")


pg = st.navigation([home, tomato, apple])
st.set_page_config(page_title="Plant Leaf Disease Classification")
pg.run()