
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
  page_title='Job market analsysis',
  page_icon = '📊'
)
# Expander section
custom_css = """
<style>
    .stTextInput input {
        border: 1px solid #C1C6CB !important;
    }
</style>
"""

# Add custom CSS to the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)
try:
  original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:500;">Good day to you, mysterious one, I would like to present you results of my analysis</p>'
  st.markdown(original_title, unsafe_allow_html=True)

  st.subheader('But firstly, follow instruction below to continue!')
  if "greet" not in st.session_state:
    st.session_state["greet"] = ""
  greet = st.text_input('Write your name, nickname or whatever and click the button!',st.session_state['greet'])
  submit = st.button("Let's go")
  if submit:
    if greet=="":
      st.session_state["greet"] = ""
    else:
      st.session_state["greet"] = greet
  if st.session_state["greet"]:
    st.write('👋 Hey ',greet,", nice to meet you!" )
    original_title = '<p style="font-family:Courier; font-size: 20px; font-weight:600;">My name is Grzegorz. As we already know each other and you are still here, I will give brief overview of this analysis, app and maybe few words about me.</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.write(' ')

    st.write('If someone is wondering...')
    with st.expander("Here I explain how I obtained data"):
      st.write("https://github.com/gregi12/job_market_analysis1/blob/main/obtaining_data.py")
   
        
except:
  pass

