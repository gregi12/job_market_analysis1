import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.lines import Line2D

# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
csv_path = os.path.join(BASE_DIR, '..', 'files', 'keywordsfull.csv')

# Wczytaj plik csv do dataframe
df = pd.read_csv(csv_path)
# Uploading dataframe


# Tabs section
st.write('Choose format of the data')
tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])

with tab1:
  
  st.subheader('Top 15 keywords by amount 📊')
  colors = ['#F21D1D', '#FD3327' ,'#0816D8', '#334CF9','#F64F20','#F7653B','#F9A04D','#FDDC48','#FFFF4F','#5167FA','#FFE580','#7788FF','#9198FF','#CED4FF','#FAF7B7'] 
  fig = plt.figure()
  plt.bar(df['keywords'], df['amount'],color=colors, edgecolor='black')
  plt.xticks(rotation=90)
  plt.ylabel('Amount')
  skills_handle = Line2D([0], [0], color='blue', label='Skills')
  tools_handle = Line2D([0], [0], color='red', label='Tools', linestyle='-',
                      marker='o', markersize=5, markerfacecolor='yellow', markeredgecolor='orange')

# Add custom legend to the plot
  plt.legend(handles=[skills_handle, tools_handle])
  # Display chart in Streamlit app
  st.pyplot(fig)
  original_title = '<p style="font-family:Courier; font-size: 20px; font-weight:600;">We clearly see that Excel is the most wanted skill in data analytics market. It was found in over 60% of descriptions. A little less demand is on sql and degree. Visualization tools like Power Bi and Tableau have high demand aswell.</p>'
  st.markdown(original_title, unsafe_allow_html=True)

  

with tab2:
# Create bar chart sorted by value
  st.subheader('Top 15 keywords by percentage 📊')
  fig = plt.figure()
  colors = ['#F21D1D', '#FD3327' ,'#0816D8', '#334CF9','#F64F20','#F7653B','#F9A04D','#FDDC48','#FFFF4F','#5167FA','#FFE580','#7788FF','#9198FF','#CED4FF','#FAF7B7'] 
  plt.bar(df['keywords'], df['percentage'],color=colors, edgecolor='black')
  
  plt.xticks(rotation=90)
  plt.ylabel('%')
  skills_handle = Line2D([0], [0], color='blue', label='Skills')
  tools_handle = Line2D([0], [0], color='red', label='Tools', linestyle='-',
                      marker='o', markersize=5, markerfacecolor='yellow', markeredgecolor='orange')

  # Add custom legend to the plot
  plt.legend(handles=[skills_handle, tools_handle])
  # Display chart in Streamlit app
  st.pyplot(fig)





with tab3:
  st.write(df)

