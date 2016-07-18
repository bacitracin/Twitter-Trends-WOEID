# Twitter-Trends-WOEID

This Python script is used to pull down the top ten Twitter trends in a given area (identified by WOEID). It appends this data to a CSV, which is the output I needed at the time. It also takes in a trend and tells you if it has trended on Twitter yet, and where. 

You don't have to start with a CSV, the program will create one in your folder. 
Once it exists, the program will append new data to the bottom of the sheet.
You can use Task Scheduler to arrange to have this run every 15 minutes, which is the 
current rate limit for Twitter.
