from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd

# Define model

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Read in dataset 

df = pd.read_csv('/filepath/filename.csv')

# Tweets that we like to encode

sentences = df["tweet"]
conspiracy = ['vaccine causes deaths']

# Sentences are encoded by calling model.encode()

embeddings1 = model.encode(sentences, convert_to_tensor=True)

# Encode conspiracy

embeddings2 = model.encode(conspiracy, convert_to_tensor=True)

# Compute cosine-similarits

cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
len(cosine_scores)

# Convert tensor dataset to list

a = cosine_scores.tolist()
df["sentence_transformers_exp"] = a

# Save to dataframe

df.to_csv('/filepath/filename.csv')
