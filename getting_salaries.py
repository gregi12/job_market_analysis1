# these 2 lines connect jupyter notebook with packages in my virtualnev. I know there's a way to add it for good but just keeped that.
#import sys
#sys.path.append(r'C:\Users\komputer\Desktop\aktualne\environment\serpapi\job_analysis\Lib\site-packages')

# So after I obtained all the data it's time to make use of it
# Here I concatenated data to 1 big DataFrame and get everything to clean form
import pandas as pd
df1 = pd.read_csv('additional.csv')
df = pd.read_csv('wszystkie.csv').drop('Unnamed: 0.1',axis=1)
df = pd.concat([df,df1])



df = df.drop_duplicates(subset=['description'])
df = df.reset_index().drop('index',axis=1)
df = df.drop('Unnamed: 0',axis=1)
df

# Clean info about site from which offer comes from 
hook = 0
for string in df['via']:
    try:
        word = string[4:]
        df['via'][hook]= word
    except:
        hook+=1
        print('Not match',hook)
    else:
        hook+=1
        
# I found better way to find all salaries
import re
hook = 0
slownik_kasy = {}
for text in df['extensions']:
    try:
        pattern = re.compile(r"'([^']*(a year|a day|a month)[^']*)'")
        wyplata = re.findall(pattern,text)
        slownik_kasy[hook] = wyplata[0]
    except:
        hook+=1
        continue
    else:
        hook+=1

# I made this dict to upload salaries in dataframe 
new_dict = {}
for key in slownik_kasy.keys():
    new_dict[key] = slownik_kasy[key][0]

import numpy as np
# Here I update cells in salaries column with my results
def update_salary(dicti):
    for key in dicti.keys():
            try:
                df['salary'][key]=dicti[key]
            except:
                print('error')
                continue
update_salary(new_dict)

# and here I make list with all desciptions to get salaries from descriptions with index of offer
wazna_lista = []
for index,x in df.iterrows():
    text = x['description']
    wazna_lista.append([index,text])
    
import re
#pattern which looks for salaries
pattern = r"£\d{1,3}(?:,\d{3})*(?:\.\d{2})? *- *£\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

results = []
# adding results to list 'results'
for item in wazna_lista:
    text = item[1]
    matches = re.findall(pattern, text)
    if matches:
        results.append([item[0], matches[0]])

print(results)

# again uploding salaries in dataframe

for index , salary in results:
    df['salary'][index] = salary

# and now I obtained all salaries     
slownik_value_dict ={}
for index, row in df.iterrows():
    if not pd.isna(row['salary']):
        slownik_value_dict[index] = row['salary']


# and now in nowa I have all salaries with index of offer
year_salary =[]
for key in slownik_value_dict.keys():
    year_salary.append(key)
year_salary
    
    
nowa = []
for key in year_salary:
    nowa.append([key,df['salary'].iloc[key]])
    
# So i had an idea and made list of lists where every sublist was like this
# first element was salary, second  was 4 last letters of salary string , so I know if it is year day hour or something diffrent
# and last element was offer index in dataframe so I can match salary with offer if some kind of problem appear
wypki =[]
for key in nowa:
    wypki.append([key[1],key[1][-4:],key[0]])
# and then I grouped it as below
funty= []
dolary = []
us = []
rest = []
def dodaj(lista):
    for key in lista:
        if key[0][0] == '£':
            funty.append(key)
        elif key[0][0]=='$':
            dolary.append(key)
        elif key[0][:2]=='US':
            us.append(key)
        else:
            rest.append(key)
            

dodaj(wypki)
# now I almost have all salaries grouped by currency
# It turned out that all results from rest are in dollars so I added them and results which first to characters were 'US' to dolary
for key in rest:
    dolary.append(key)
for sublt in us:
    dolary.append(sublt)

# so I started with pounds
funty_extended= []
for key in funty:
    index = key[2]
    new = [key[0],key[1],key[2],df['title'][index],df['location'][index]] #
    funty_extended.append(new)  

funt_counts = {}
# in funt_counts I have salary and how many times it appeared
for row in funty_extended:
    if row[0] in funt_counts:
        funt_counts[row[0]] += 1
    else:
        funt_counts[row[0]] = 1
        
# Iterowanie po liście stringów i usuwanie przecinków z wypłat
no_commas_listaa = []
for key ,value in funt_counts.items():
    no_commas = key.replace(",", "")
    if no_commas[-4:]=='year':
        no_commas_listaa.append([no_commas[:-7],value,'year'])
        hook+=1
    elif no_commas[-3:]=='day':
        no_commas_listaa.append([no_commas[:-6],value,'day'])
        hook+=1
    else:
        no_commas_listaa.append([no_commas,value,'else'])

# Here we already have divided results for salary per year, per day and rest
year_list = []
day_list = []
rest_list = []
for words in no_commas_listaa:
    try:
        if words[2]== 'year':
            year_list.append([words[0],words[1]])
        elif words[2] =='day':
            day_list.append([words[0],words[1]])
        elif words[2]== 'else':
            rest_list.append([words[0],words[1]])
        
            
    except:
        print('trudno')
# some manual work to get salary per day , because these results went to rest due to no day word at the end 
# so I did it manually
day_list.append(['£55-£65', 1])
day_list.append(['£350 - £400', 1])
day_list.append(['£70-£80', 1])
day_list.append(['£600 - £680', 1])

# of course these which I added to day list i had to remove from rest list

rest_list.pop(6)
rest_list.pop(8)
rest_list.pop(12)
rest_list.pop(-12)
rest_list.pop(-6)

# and rest of results was salary per year so I added it to year_list
for key in rest_list:
    year_list.append([key[0],key[1]])
year_list

# so I had year and day list already.
#then I formatted 9 results from day list to year format: I multiplied it by 260 (amount of workdays in year)
dni_rok = [['104000',1],['156000-176000',1],['104000-119000',1],['105000',1],['52000',1],['156000-182000',1],['100000',1],['17000',1],['20000',1]]

#added them to year_list
for key in dni_rok:
    year_list.append(key)
year_list.append(['15000',1])
# Then removed all unnecessary characters and replaced K with 000 so everything is in same format now
cleaner_funty=[]
for key in year_list:
    jo = key[0].replace('K','000').replace('T','000').replace('£','').replace('–','-')
    cleaner_funty.append([jo,key[1]])
# I had to manually change 1 result
cleaner_funty.remove(['42.3000', 1])
cleaner_funty.append(['42300',1])
# and here I splitted salary ranges on '-' and took average of everything in final_aver_funty and how many specific salary happend in ranges.
ranges = []
final_aver_funty=[]
for key in cleaner_funty:
    if len(key[0])<=6:
        jo = round(float(key[0]))
        jo2 = round(float(jo))*key[1]
        final_aver_funty.append(jo2)
        ranges.append([jo,key[1]])
    else:
        
        jo = key[0].split('-')
        first = round(float(jo[0]))
        second = round(float(jo[1]))
        aver = (first+second)/2
        aver_sum = aver*key[1]
        final_aver_funty.append(aver_sum)
        ranges.append([aver,key[1]])
        
# this is average salary in pounds 44559   (it's 54807 in USD)    
sum(final_aver_funty)/120

# now last thing is to get how many times specific range occured. I divided all of ranges into 2 groups as below.
over_100=[]
under_100=[]
for key in ranges:
    if key[0]>=100000:
        over_100.append(key)
    else:
        under_100.append(key)
     
# and made dict with instances of every range. Ranges are from 10k-20k, 20k-30k etc.       
counts_funty ={}
for item in under_100:
    range_num = str(item[0])
    range_num = range_num[0]
    if range_num in counts_funty:
        counts_funty[range_num] += item[1]
    else:
        counts_funty[range_num] = item[1]
        
for item in over_100:
    range_num = str(item[0])
    range_num = range_num[0:2]
    if range_num in counts_funty:
        counts_funty[range_num] += item[1]
    else:
        counts_funty[range_num] = item[1]
        
# and it's finished. I won't show how I've dealt with dollars because it's basically the same. 
counts_funty
