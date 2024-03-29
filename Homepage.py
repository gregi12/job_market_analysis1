
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
  
  original_title = '<p style="font-family:Courier; font-size: 20px; font-weight:600;">My name is Grzegorz. If you are still here, I will give brief overview of this analysis, app and maybe few words about me.</p>'
  st.markdown(original_title, unsafe_allow_html=True)
  st.write(' ')

  st.write('If someone is wondering...')
  with st.expander("Here I explain how I obtained data"):
    st.write("https://github.com/gregi12/job_market_analysis1/blob/main/obtaining_data.py")

     # Tworzenie trzech przycisków w trzech kolumnach
  col1, col2, col3 = st.columns(3)

  # Dodawanie przycisków do kolumn
  with col1:
    button1 = st.button("About analysis")
    if button1:
      original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;">Sooo, these results comes from over 1200 job offers. Above is link to github file where I give more detailed explanation about how I obtained the data. I extracted valuable data using regular expressions (regex)</p>'
      st.markdown(original_title, unsafe_allow_html=True)
      with st.expander("More info here!"):
        st.write("https://github.com/gregi12/job_market_analysis1/blob/main/getting_keywords.py")
  with col2:
    if st.button("About app"):
      original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;">In upper left corner you can see navigation links, every one of them is for specific part of visualization . Whenever there is info about percentage , it means percentage of all offers after duplicates were deleted, so eventually on 994 offers. If not, then I give additional info . I would suggest to use light theme , everything is more clear then. Theme can be changed in settings in upper right corner</p>'
      st.markdown(original_title, unsafe_allow_html=True)
        

  with col3:
    if st.button("About me"):
      original_title = "<p style='font-family:Calibri; font-size: 20px; font-weight:600;'> I'm a young person with a lot of energy and ideas. I am kind of guy who looks for patterns everywhere. In high school I was laureate of district-level math competition (there were only about 80 students in my voivodeship with the same status). For some time I'm catching up with statistics and linear algebra. In the future I want to work in as a Data Analyst or in AI industry   </p>"
      st.markdown(original_title, unsafe_allow_html=True)
 
        
except:
  pass
  
