# -*- coding: utf-8 -*-
"""
Created on Wednesday May 13 13:00:14 2015

@author: getTrends function modified from trends.py 
original script: https://gist.github.com/alienone/9349702

Modified by Tracy to create and update a CSV with top 10 Twitter trends.
Index refers to the 1 - 10 trending topic ranking. 15 is 5th, 23 is 3rd, etc.

You don't have to start with a CSV, program will create one in your folder. 
Once it exists, the program will append new data to the bottom of the sheet.
Use Task Scheduler to arrange to have this run every 15 minutes, which is the 
current rate limit for Twitter.

"""
# Pip install these modules if you don't already have them
from twython import Twython
from urllib2 import unquote 
import pandas as pd
        
# Please use your own Twitter credentials, found at apps.twitter.com.
APP_KEY = "C0mughtR15ab8e06qGQbVjmLF"
APP_SECRET = "GOgphYsPfh3jR4JYLH6s0GPrq0wdzQr1IpwSKqidnqXxh1Fd7W"
OAUTH_TOKEN = "227459435-IHYybp0wrxGKV8WrgYyECFJ9osyx1dgvNttR2ilc"
OAUTH_TOKEN_SECRET = "fy5ezX1A3uRESUKnsjFniZQgWKxfoqySBlJJkwdBaBmLw"

# Yahoo WOEIDs, you can specify by city, address, zip code, state country... 
# See more here: http://woeid.rosselliot.co.nz/lookup/
woeid_list = [('World', 1),
             ('USA', 23424977)]
            #('UK', 23424975),
            #('France', 23424819),
            #('Italy', 23424853),
            #('Germany', 23424829),
            #('Spain', 23424950),
            #('Mexico', 23424900),
            #('Australia', 23424748),
            #('New Zealand', 23424916), 
            #('Canada', 23424775),
            #('Brazil', 23424768)
           # ]  

def getTrends(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, woeid_list):
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    list_of_tuples = []    
    for item in woeid_list:
        place_name = item[0]
        place_woeid = item[1]
        place_trend_list = twitter.get_place_trends(id=place_woeid)
        for item in place_trend_list:
            for element in item['trends']:
                place_tuple =(place_name, place_woeid, element['name'], item['created_at'])
                list_of_tuples.append(place_tuple)
    return list_of_tuples


def trend_list_parsing():       
    list_of_trend_results=[]   
    for trend in get_trends_results:
        trend_date = trend[3]
        trend_location = trend[0]
        trend_woeid = trend[1]
        trend_name = (unquote(trend[2]))
        trend_tuple = (trend_date, trend_location, trend_woeid, trend_name)
        list_of_trend_results.append(trend_tuple)
    return list_of_trend_results


def is_it_trending(name_of_trend):
    hashtag_trend = '#' + name_of_trend
    x = item_dataframe.loc[item_dataframe.Hashtag.values == (name_of_trend)]
    if x.empty:
        y = item_dataframe.loc[item_dataframe.Hashtag.values == (hashtag_trend)]
        if y.empty:
            print('Not currently trending!')
        else:
            print(name_of_trend + ' is currently trending in the following places')    
            print(y)
    else:
        print(name_of_trend + ' is currently trending in the following places')    
        print(x)

# Getting the data
get_trends_results = getTrends(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, woeid_list)  
trend_data = trend_list_parsing()

# Throwing it in a dataframe
item_dataframe = pd.DataFrame(trend_data) 
item_dataframe.columns = ['Date', 'Place', 'WOEID', 'Hashtag']
# To see what's in the dataframe without checking the CSV, 
#just type "item_dataframe" into the console.


# Appending the dataframe to a CSV. Edit the CSV name here.
with open('Testingtesting.csv', 'a') as fd:             
    item_dataframe.index += 1        
    item_dataframe.to_csv(fd, mode='a',header=False, encoding='utf-8')
    fd.close()

# Fill in your trend here. It should work with and without hashtags.
is_it_trending('ThinkContent')
        
        
        
        
        
  
