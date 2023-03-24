# So after I obtained all the data it's time to make use of it
# Here I concatenated data to 1 big DataFrame and get everything to clean form
import pandas as pd
df1 = pd.read_csv('additional.csv')
df = pd.read_csv('wszystkie.csv').drop('Unnamed: 0.1',axis=1)
df = pd.concat([df,df1])


# 
df = df.drop_duplicates(subset=['description'])
df = df.reset_index().drop('index',axis=1)
df = df.drop('Unnamed: 0',axis=1)
df

nested_list = ['senior','developing\\sreports','sql', 'database', 'data\\smanagment', 'junior', 'gcp', 'college\\sdegree',
               'degree', 'computer\\sEngineering', 'reports', 'expert\\slevel', 'Power\\sBi', 
               'tableau', 'powerBI', 'mySql', 'pandas', 'numPy','google\\scloud'
                'matplotlib', 'seaborn', 'linux', 'windows', 'gcloud', 'azure', 'excel', 'tensorflow', 'keras', 'git', 'SSRS', 'SSIS', 'ETL', 'Snowflake', 'UNIX'
            ,'SSMS', 'Visual\\sStudio', 'SharePoint', 'JIRA', 'python', 'data\\smining', 'data\\sMining', 'application\ssDesign', 'application\\sdesign',
               'business\\sIntelligence',
               'information\\smanagement',
               'excellent\sscommunication', 'interpersonal\\sskills', 'maintain\\sdata\\ssets', 'data\\sbase\\sdevelopment', 
               'maintain\\sdatabases', 'Extracting\\sdata', 'data\\swarehouse', 'agile', 'scrum', 'Excellent\\sverbal\\sand\\swritten']

# this function loops every description in given dataframe and looks for all keywords from nested list
def get_keywords(data):
    lista_keywords = []
    for desc in data['description']:
        try:
            for phrase in nested_list:
                try:
                    pattern = re.compile(f'{phrase}', re.IGNORECASE)
                    words = pattern.findall(desc)
                    lista_keywords.append(words[0]) #Notice that I add only 1 results for each description to 
                    hook+=1                           # avoid getting 30 'excels' from 1 offer for example

                except:
                    continue
        except:
            continue
    return lista_keywords

lista_keywords = get_keywords(df)

# Here I make set from this list so I got back all unique keywords 
#
set_keywords = set(lista_keywords)

#here I got dict with keywords and how many times they appeared 
import operator
ostateczny_slownik = (dict((x,lista_keywords.count(x)) for x in set_keywords))


# I make one big list as below to match all keywords no matter of letter sizes

lista_laczna = list([key,value] for key,value in ostateczny_slownik.items())

# Thanks to that I could sum all words regardless of size of letters

word_count = {}

for sublist in lista_laczna:
    word = sublist[0].lower()
    count = sublist[1]
    
    if word in word_count:
        word_count[word] += count
    else:
        word_count[word] = count
# And finally we got all keywords sorted 
slownik = dict(sorted(word_count.items(), key=operator.itemgetter(1),reverse=True ))

# then I just took 15 top keywords(before this I concatenated powerbiand power bi), added them to dataframe and that's it
