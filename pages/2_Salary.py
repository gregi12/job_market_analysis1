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