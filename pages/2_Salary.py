import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
dolary_path = os.path.join(BASE_DIR, '..', 'files', 'dolary.csv')
funty_path = os.path.join(BASE_DIR, '..', 'files', 'funty.csv')
# Wczytaj plik csv do dataframe
df = pd.read_csv(dolary_path)
# Uploading dataframe
df1= pd.read_csv(funty_path)

st.write('Choose currency or overall')
tab1, tab2 , tab3= st.tabs(["Dollars", "Pounds", "Avearge salary"])

with tab1:
    st.subheader('Top 15 keywords by amount 📊')
    colors = ['r', 'b', 'g'] + ['grey'] * 12
    fig = plt.figure()
    plt.bar(df['salary'], df['amount'],color=colors, edgecolor='black')
    plt.xticks(rotation=90)
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)