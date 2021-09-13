# install twint, nest_asyncio
! pip install -qq twint
! pip install -qq nest_asyncio

#import pandas and twint
import pandas as pd
import twint
import nest_asyncio
nest_asyncio.apply()

# Read in dataset

data = pd.read_csv('/filepath/filename.csv')

# Simple classifier function 

def classify(tweet):
    classified = [1 if "vaccine causes death" in tweet else 0]
    return classified

# regex classifier to see whether tweets contain  

simple_classifier = data['tweet'].apply(lambda x: classify(x))

# Add column onto dataset 

data["simple_classifier"] = simple_classifier

# Save dataset to Documents

data.to_csv('/filepath/filename.csv')
