import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
csv_path = os.path.join(BASE_DIR, '..', 'files', 'Typefull.csv')

# Wczytaj plik csv do dataframe
df = pd.read_csv(csv_path)

tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])

with tab1:
    st.subheader('Types of contract 📊')
    fig = plt.figure()
    colors = ['#D2042D', '#702963', '#C04000','#8F8585'] 
    plt.bar(df['Type'], df['Amount'],color=colors,edgecolor='black',linewidth=1)
    plt.xticks(rotation=45)
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)

with tab2:
    st.subheader('Types of contract 📊')
    labels = [key for key in df['Type'][:2]]
    labels.append('Rest')
    keys = [key for key in df['Percentage'][:2]]
    keys.append(1.83)
    colors = ['#E80C0C', '#05D832', '#F1FC00'] 
    explode = (0.1,0,0)
    fig, ax = plt.subplots()
    
    ax.pie(keys, labels=labels, 
          startangle = 0,
          autopct='%1.1f%%',
          colors=colors,
          explode=explode
          )
    
    st.pyplot(fig)


with tab3:
    st.write(df)
    
