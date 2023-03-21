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

df1= pd.read_csv(funty_path)

st.write('Choose currency or overall')
tab1, tab2 , tab3,tab4= st.tabs("Overview","Dollars", "Pounds", "Avearge salary")
with tab1:
    st.write("Here is code which took us from something like this: '£35,000 - £55,000','£30K–£41K a year', '45–75 an hour','70K–80K a year', '$75K–$85K a year' to what you see in next tabs. ")
    st.expander()
    
with tab2:
    st.subheader('Salary ranges in dollars 📊')
    colors = ['r', 'b', 'g'] + ['grey'] * 12
    fig = plt.figure()
    plt.bar(df['salary'], df['amount'],color=colors, edgecolor='black')
    plt.xticks(rotation=90)
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)

with tab3:
    st.write('Here are offers which originally were in £' )
    st.subheader('Salary ranges in pounds 📊')
    colors = ['r', 'b', 'g'] + ['grey'] * 12
    fig = plt.figure()
    plt.bar(df1['salary'], df1['amount'],color=colors, edgecolor='black')
    plt.xticks(rotation=90)
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)

with tab4:
    
    st.subheader('Average salary 📊')
    st.write('So at the end there were 102 offers in USD and 119 was in Pounds. So I made 3 sections with offers from US, from UK and overall.')
    colors = ['r', 'b', 'g']
    fig = plt.figure()
    plt.bar(["Offers from US","Offers from UK","All offers in USD"], ['$90246','$53534','$70477'],color=colors, edgecolor='black')
    plt.xticks(rotation=90)
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)