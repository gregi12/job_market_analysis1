import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
csv_path = os.path.join(BASE_DIR, '..', 'files', 'Work_home_perce.csv')

# Wczytaj plik csv do dataframe
df = pd.read_csv(csv_path)

tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])

with tab3:
    st.write(df)