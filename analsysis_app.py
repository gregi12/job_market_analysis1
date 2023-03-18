
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
mpl.style.use('classic')
st.set_page_config(
  page_title='Job market analsysis',
  page_icon = '📊'
)
# Expander section
try:
  original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:500;">Good day to you, mysterious one, I would like to present you results of my analysis</p>'
  st.markdown(original_title, unsafe_allow_html=True)

  # Sidebar section
  with st.sidebar:
    st.subheader('This is a Sidebar')
    st.write('Button with Balloons 🎈')
    if st.button('Click me!✨'):
      st.balloons()
    else:
      st.write(' ')



  st.subheader('But firstly, follow instruction below to continue!')
  if "greet" not in st.session_state:
    st.session_state["greet"] = ""
  greet = st.text_input('Write your name, nickname or whatever!',st.session_state['greet'])
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
      st.write("https://github.com/gregi12/Jobs-offers-project/blob/master/getting_data.py")
      # Tworzenie trzech przycisków w trzech kolumnach
    col1, col2, col3 = st.beta_columns(3)

    # Dodawanie przycisków do kolumn
    with col1:
      button1 = st.button("About analysis")
      if button1:
        original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;">Sooo, these results comes from over 1200 job offers. Above is link to github file where I give more detailed explanation about how I obtained the data. I extracted valuable data using regular expressions(regex)</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        with st.expander("More info here!"):
          st.write("https://github.com/gregi12/Jobs-offers-project/blob/master/final_analysis.py")
    with col2:
      if st.button("About app"):
        original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;">In upper left corner you can see navigation links, every one of them is for specific part of visualization . Whenever there is info about percentage , it means percentage of all offers after duplicates were deleted, so eventually on 994 offers. If not, then I give additional info . I would suggest to use light theme , everything is more clear then. Theme can be changed in settings in upper right corner</p>'
        st.markdown(original_title, unsafe_allow_html=True)
          

    with col3:
      if st.button("About me"):
        original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;"></p>'
        st.markdown(original_title, unsafe_allow_html=True)
except:
  pass

