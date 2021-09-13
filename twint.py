#install twint, nest_asyncio
! pip install -qq twint
! pip install -qq nest_asyncio

import pandas as pd
import twint
import nest_asyncio
nest_asyncio.apply()

## Setting up twint configuration 

c = twint.Config()

## Extracting data from Twitter
## Twint parameters help to filter search 

def scrape_new_topic(keyword, filename):
    c.Search=keyword
    c.Since="2021-05-01"
    c.Until="2021-05-03"
    ## c.Near="london"
    c.Lang="en"
    ## c.Min_likes = 2
    c.Pandas=True
    c.Limit=200
    c.Store_csv=True
    c.Output= "../" + filename + ".csv"
    twint.run.Search(c)

## Scrape new dataset

keyword = "5G vaccine"
filename = "vaccine_5G_set_20Jul"
scrape_new_topic(keyword, filename)
