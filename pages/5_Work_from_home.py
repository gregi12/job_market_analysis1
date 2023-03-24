import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
png_path = os.path.join(BASE_DIR, '..', 'files', 'out.png')


tab1, tab2 = st.tabs(["Quantity", "Percentage"])
with tab1:
    st.image(png_path)

with tab2:

    # Data for the pie chart
    labels = ['No', 'Yes']
    sizes = [79, 21]
    colors = ['#66b3ff', '#ff9999']

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

    # Set the title
    ax.set_title('Work From Home')

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')
    st.pyplot(fig)
