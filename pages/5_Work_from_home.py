import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
png_path = os.path.join(BASE_DIR, '..', 'files', 'out.png')


tab1, tab2 = st.tabs(["Quantity", "Percentage"])
with tab1:
    st.image(png_path)
with tab2:
    data = {"work_from_home":[21,79]}
    df = pd.DataFrame(data)
    sns.set(style='whitegrid')
    plt.figure(figsize=(10, 6))  # Adjust the figure size
    ax = sns.barplot(x='work_from_home', y='percentage', data=df)
    ax.set(xlabel='work from home', ylabel='percentage', title='work from home')
    st.pyplot(ax)

   
