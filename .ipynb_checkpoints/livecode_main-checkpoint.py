import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Hello class!')


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Sales", "Finance", "HR")
    )

# Using "with" notation
#with st.sidebar:
 #   add_radio = st.radio(
  #      "Choose a shipping method",
   #     ("Sales", "Finance")
    #)
    
[theme]
base = "dark"
primaryColor="#F63366"

if add_selectbox == 'Sales':
    st.markdown('''Welcom to *Sales*''')
elif add_selectbox == 'HR':
    st.markdown('''Hi_This is_**HR**''')
else:
    st.markdown('Hellooo')
#comment
