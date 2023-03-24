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
# paths to images
dolary_path = os.path.join(BASE_DIR, '..', 'files', 'dolary.png')

funty_path = os.path.join(BASE_DIR, '..', 'files', 'funty.png')

st.write('Choose currency or overall')
tab1,tab2,tab3,tab4= st.tabs(["Overview","Dollars", "Pounds", "Average salary"])
with tab1:
    original_title = "<p style='font-family:Calibri; font-size: 20px; font-weight:600;'>Below is link to code which took us from something like this: '£35,000 - £55,000', '£30K–£41K a year', '45–75 an hour', '70K–80K a year' to what you can see in next tabs. In short, after I got salaries from offers using regular expressions, I divided data into USD and pound lists, then divided even further to year, day hour etc. . In next step, I took average and how many times specific range occurred. As u see, there were a lot of diffrent formats so I took this approach: If there was range , I took sum of first and second element and dividied it by 2. If not, I just used single value as average. If salary was per hour, I  multiplied it by 2080 (8 hours per day, 260 workdays in year as google says) </p>"
    st.markdown(original_title, unsafe_allow_html=True)
    with st.expander('Check if u want!'):
        st.write('https://github.com/gregi12/job_market_analysis1/blob/main/getting_salaries.py')

    
with tab2:
    st.subheader('In the right corner of chart, there is a button to turn on fullscreen if needed 📊')
    st.image(dolary_path)
    # colors = ['r', 'b', 'g'] + ['grey'] * 12
    # fig = plt.figure()
    # plt.bar(df['salary'], df['amount'],color=colors, edgecolor='black')
   # plt.xticks(rotation=90)
  #  plt.ylabel('Amount')
    # Display chart in Streamlit app
    # st.pyplot(fig)

with tab3:
    st.image(funty_path)
with tab4:
    
    st.subheader('Average salary 📊')
    st.write("At the end there were 102 offers in USD and 120 was in pounds and that's strange because most of offers were from US. It looks like, in UK ,employers more willingly give informations about salary . I decided to make 3 sections with offers from US, from UK and overall.")
    colors = ['r', 'b', 'g']
    fig = plt.figure()
    plt.bar(["Offers from US","Offers from UK","All offers in USD"],height= [90246,53534,70477],color=colors, edgecolor='black')
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)