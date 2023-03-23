import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

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
  colors = ['#F21D1D', '#F12923' , '#2439E1','#2962F8','#F64F20','#F7653B','#F8CA29','#FDDC48','#FFFF4F '] 
  fig = plt.figure()
  plt.bar(df['keywords'], df['amount'],color=colors, edgecolor='black')
  plt.xticks(rotation=90)
  plt.ylabel('Amount')
  # Display chart in Streamlit app
  st.pyplot(fig)
  original_title = '<p style="font-family:Courier; font-size: 20px; font-weight:600;">We clearly see that Excel is the most wanted skill in data analytics market. It was found in over 60% of descriptions. A little less demand is on sql and degree. Visualization tools like Power Bi and Tableau have high demand aswell.</p>'
  st.markdown(original_title, unsafe_allow_html=True)

  

with tab2:
# Create bar chart sorted by value
  st.subheader('Top 15 keywords by percentage 📊')
  fig = plt.figure()
  colors = ['#FF0909', 'b', 'g'] + ['grey'] * 12
  plt.bar(df['keywords'], df['percentage'],color=colors, edgecolor='black')
  # ustawienie kolorów słupków
  plt.xticks(rotation=90)
  plt.ylabel('%')

  # Display chart in Streamlit app
  st.pyplot(fig)





with tab3:
  st.write(df)

