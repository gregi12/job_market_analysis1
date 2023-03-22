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
tab1,tab2,tab3,tab4= st.tabs(["Overview","Dollars", "Pounds", "Average salary"])
with tab1:
    st.write("Below is link to code which took us from something like this: '£35,000 - £55,000','£30K–£41K a year', '45–75 an hour','70K–80K a year' to what you can see in next tabs. In short, after I got salaries from descriptions using regular expressions, I divided data into USD and pound lists, then divied even further to year, day hour etc. .  and then took average and how many times specific range appeared. As u see there were a lot of diffrent formats so I took this approach: If there was range , I took sum of first and second element and dividied it byt 2. If not, i jsut used single value as average. ")
    with st.expander('Check if u want!'):
        st.write('https://github.com/gregi12/job_market_analysis1/blob/main/getting_salaries.py')

    
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
    st.write('Here are offers which originally were in pounds' )
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
    st.write("At the end there were 102 offers in USD and 120 was in pounds and that's strange because most of offers were from US. It looks like, in UK ,employers more willingly give informations about salary . I decided to make 3 sections with offers from US, from UK and overall.")
    colors = ['r', 'b', 'g']
    fig = plt.figure()
    plt.bar(["Offers from US","Offers from UK","All offers in USD"],height= [90246,53534,70477],color=colors, edgecolor='black')
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)