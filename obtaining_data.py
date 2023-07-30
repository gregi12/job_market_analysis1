# So at the beggining it looked like this, that was my first research for this project
# I was searching for about 100 results daily

from serpapi import GoogleSearch
import numpy as np
import pandas as pd
import datetime
api_key = # your_api_key from serpapi

for num in range(10):
            # This is like page number of results but it's multiplied by 10
            start = num * 10
            search_loc = 'United States'

            search = GoogleSearch({
            "q":'data analyst', #Term which we are looking for
            "api_key":api_key , # Your unique API key
            "device":'desktop',
            "engine":'google_jobs',
            'hl':'en',
            'location':search_loc,
            'chips':'date_posted:today',
            'start':start,
            })

            # check if the last search page (i.e., no results)
            results = search.get_dict()
            try:
                if results['error'] == "Google hasn't returned any results for this query.":
                    break
            except KeyError:
                print(f"Getting SerpAPI data for page: {start}")
            else:
                continue

            #converting into Data frame

            jobs_df = results['jobs_results']
            jobs_df = pd.DataFrame(jobs_df)
            jobs = pd.concat([pd.DataFrame(jobs_df),
                               pd.json_normalize(jobs_df['detected_extensions'])],
                               axis=1).drop('detected_extensions',1)
            jobs['date_time'] = datetime.datetime.utcnow()

            #concat DataFrame
            if start == 0:
                jobs_all = jobs
            else:
                jobs_all = pd.concat([jobs_all, jobs])

            jobs_all['search_term'] = 'data analyst'
            jobs_all['search_location'] = search_loc


# later I put it into function do_stuff()

def do_stuff():
    from serpapi import GoogleSearch
    import numpy as np
    import pandas as pd
    import datetime
    api_key = 'd9e1f7d32270c69ad8a9a1a657a16bc1fc98e3c32d6b99fd67c1d2167d66790b'

    for num in range(10):

        start = num * 10
        search_loc = 'United States'

        search = GoogleSearch({
        "q":'data analyst',
        "api_key":api_key ,
        "device":'desktop',
        "engine":'google_jobs',
        'hl':'en',
        'location':search_loc,
        'chips':'date_posted:today',
        'start':start,
        })

        # check if the last search page (i.e., no results)
        results = search.get_dict()
        try:
            if results['error'] == "Google hasn't returned any results for this query.":
                break
        except KeyError:
            print(f"Getting SerpAPI data for page: {start}")
        else:
            continue

        #converting into Data frame

        jobs_df = results['jobs_results']
        jobs_df = pd.DataFrame(jobs_df)
        jobs = pd.concat([pd.DataFrame(jobs_df),
                           pd.json_normalize(jobs_df['detected_extensions'])],
                           axis=1).drop('detected_extensions',1)
        jobs['date_time'] = datetime.datetime.utcnow()

        #concat DataFrame
        if start == 0:
            jobs_all = jobs
        else:
            jobs_all = pd.concat([jobs_all, jobs])

        jobs_all['search_term'] = 'data analyst'
        jobs_all['search_location'] = search_loc
    
    return jobs_all
#And everyday I looked for new job offers and added them to csv file as below, by concatenating
# in df are new searches and in df1 are previous results
df = do_stuff()
df1 = pd.read_csv('analiza-ofert.csv')
result = pd.concat([df,df1])

# Saving all results to csv file
result.to_csv('analiza-ofert.csv')

#At the end I added all the data to my database to ensure I won't lose anything by mistake
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/oferty_pracy')
df2.to_sql('oferty',con=engine,index=False,if_exists='append')
