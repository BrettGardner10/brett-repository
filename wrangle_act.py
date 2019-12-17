#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import requests
import os
import json
import time


# <font size='5'><b>1. Data Gathering</b></font>

# In[9]:


#create dataframe by reading csv
df = pd.read_csv("twitter-archive-enhanced.csv")
df.head(2)


# Need to create and save a file down. Also need to creat the .txt file for the data.m

# In[10]:


# we know the url
tweet_image_prediction_url = "https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv"

# request from the url
folder = "data"
r = requests.get(tweet_image_prediction_url)
if r.status_code == requests.codes.ok:
    # to make sure to use utf-8 encoding
    r.encoding = 'utf-u' 

    # to store the file as a TSV file
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(os.path.join(folder, 'tweet_image_predictions.txt'), 'w') as infile:
        # write the text into the txt file
        infile.write(r.text)


# In[11]:


#open tsv file
images = pd.read_table('tweet_image_predictions.txt', sep='\t')
images.head(2)


# In[12]:


#creating an API object so we can gather Twitter data

import tweepy

consumer_key = 'Iorx4UF5DfzdCXoDNI3LA4zKX'
consumer_secret = 'gFELLACIIcPti3OxfHvF9SjfQYRkYgZE0Pr0zOBDQxexCHPvqe'
access_token = '2168888629-o9AyvMXXBFRPNnDIhTDjNQnAXQZI5esPBsX6IiD'
access_secret = 'iln7CAWqMxYGPZzBRlItDWlCVBosRXkVvmQqwJNhpQ0ZG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


# In[13]:


# create api object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,
                 parser=tweepy.parsers.JSONParser())


# In[ ]:





# In[21]:


# get the tweet IDs from the we_rate_dogs and image predictions dataframes
tweet_IDs = np.array(df['tweet_id'].values, dtype = str)
tweet_IDs = np.concatenate((np.array(tweet_image_prediction_url['tweet_id'].values,
                                     dtype = str), tweet_IDs))
tweet_IDs = np.unique(tweet_IDs)


# In[ ]:


# get the tweets
tweets = {}

for tweet_id in tweet_IDs:
    start = time.time()
    try:
        tweets[tweet_id] = api.get_status(tweet_id, tweet_mode = 'extended')
    except tweepy.TweepError as e:
        print(e)
    end = time.time()
    request_time = end - start
    print("time required: ", request_time)


# In[ ]:


# store each tweet of JSON data in a file called tweet_json.txt file
with open(os.path.join(folder, 'tweet_json.txt'), 'w', encoding='utf-8') as outfile:
    for key, value in tweets.items():
        json.dump(value, outfile)
        outfile.write('\n') # data should be written to its own line   


# In[ ]:


tweet_ids = list(df.tweet_id)

tweet_data = {}
for tweet in tweet_ids[:5000]:
    try:
        tweet_status = api.get_status(tweet, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        tweet_data[str(tweet)] = tweet_status._json
        #print(tweet_ids.index(tweet) + 1, "/", "2354")
    except:
        print("Error for: " + str(tweet))
        #print(tweet_ids.index(tweet) + 1, "/", "2354")


# In[ ]:


with open('tweet_json.txt', 'w') as file:
    json.dump(tweet_data, file)


# In[ ]:


with open('tweet_json.txt') as file:
    data = json.load(file)
    
df_list = []

for tweet_id in data.keys():
    retweets = data[tweet_id]['retweet_count']
    favorites = data[tweet_id]['favorite_count']# + data[tweet_id]['favourites_count']
    df_list.append({'tweet_id': tweet_id,
                        'retweets': retweets,
                        'favorites': favorites})
    
tweets_df = pd.DataFrame(df_list, columns = ['tweet_id', 'retweets', 'favorites'])
tweets_df.sample(5)


# Assessment

# 3 dataframes
# df = text, rating, dog category
# tweet_df = has the retweets and favorites
# images = has the neural network results

# In[ ]:


df.info()


# In[ ]:


images.info()


# In[ ]:


tweet_df.info()


# In[ ]:


df.describe()


# In[ ]:


images.describe()


# In[ ]:


tweet_df.describe()


# In[ ]:


df_clean=df.copy()
images_clean=images.copy()
tweet_df_clean=tweet_df.copy()


# In[ ]:


#go back through
archive_df_clean.tweet_id = df_clean.tweet_id.astype(str)
img_pred_clean.tweet_id = img_pred_clean.tweet_id.astype(str)
merged_df_clean = pd.merge(archive_clean, tweets_clean,
                        how = 'inner', on = 'tweet_id')
merged_df_clean = pd.merge(archive_clean, img_pred_clean,
                        how = 'inner', on = 'tweet_id')


# In[ ]:





# In[ ]:





# In[ ]:




