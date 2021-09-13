import torch
import numpy
import matplotlib.pyplot as plt

# Ensure transformers==2.8.0 is installed
!pip install transformers==2.8.0

!wget https://developer.nvidia.com/compute/cuda/9.2/Prod/local_installers/cuda-repo-ubuntu1604-9-2-local_9.2.88-1_amd64 -O cuda-repo-ubuntu1604-9-2-local_9.2.88-1_amd64.deb
!dpkg -i cuda-repo-ubuntu1604-9-2-local_9.2.88-1_amd64.deb
!apt-key add /var/cuda-repo-9-2-local/7fa2af80.pub
!apt-get update
!apt-get install cuda-9.2

# Read in file
df = pd.read_csv('filename.csv')

# Define model

from bert_nli import BertNLIModel
bert_type = 'bert-base'
model = BertNLIModel('output/{}.state_dict'.format(bert_type), bert_type=bert_type)

# Define bert_nli funcition 

def bert_nli(tweet) :
    sent_pairs = [(tweet, 'vaccine causes death')]
    label, _= model(sent_pairs)
    return label

df["nli"] = df.apply(lambda x: bert_nli((x['tweet'])), axis=1)

# Save dataset

df.to_csv('filename.csv')
