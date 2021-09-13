import pandas as pd
from textdistance import levenshtein
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string

nltk.download("stopwords")
stopwords = stopwords.words('english')
ps= nltk.PorterStemmer()

# Read in dataset 

df = pd.read_csv('/filepath/filename.csv')

# Add new column to dataframe 

df["levenshtein_conspiracy"] = 'vaccine causes death'

# Use levenshtein to calculate the distance between tweet and seed conspiracy and add in new column called lev_results

df["lev_classifier_pharma"] = df.apply(lambda x: levenshtein.distance(x['tweet'],  x['levenshtein_conspiracy']), axis=1)

# Method to convert levenshtein distance into a probability number out of 1

def levenshtein_probability(query, tweet, distance):
    bigger = max(len(query), len(tweet))
    answer = (bigger - distance)/ bigger
    return answer

# Apply levenshtein_probability method to dataset

df["normalised_lev_2"] = df.apply(lambda x: levenshtein_probability((x['levenshtein_pharma']), x['tweet'], x['lev_classifier_norm_pharma']), axis=1)

# Save dataset with new column

df.to_csv('/filepath/filename.csv')
