import streamlit as st

home = st.Page("home.py", title="Home Page")
tomato = st.Page("tomato.py", title="Tomato Leaf Disease")
apple = st.Page("apple.py", title="Apple Leaf Disease")
bellpepper = st.Page("bellpepper.py", title="Bell Pepper Leaf Disease")
corn = st.Page("corn.py", title="Corn Leaf Disease")
grape = st.Page("grape.py", title="Grape Leaf Disease")
peach = st.Page("peach.py", title="Peach Leaf Disease")
potato = st.Page("potato.py", title="Potato Leaf Disease")
strawberry = st.Page("strawberry.py", title="Strawberry Leaf Disease")



pg = st.navigation([home, tomato, apple, bellpepper, corn, grape, peach, potato, strawberry])
st.set_page_config(page_title="Plant Leaf Disease Classification")
pg.run()