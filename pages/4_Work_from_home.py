import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
png_path = os.path.join(BASE_DIR, '..', 'files', 'out.png')


tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])
with tab1:
    st.write(png_path)
    
    

with tab3:
    st.write(df)