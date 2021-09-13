# Imports

from sklearn.metrics import confusion_matrix
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sn

# Load dataframe
 
df = pd.read_csv('../twint/dataset.csv')

# Get classifier predicted values in csv

y_pred = df["bert_nli_results"]

# Get results

confusion_matrix(y_true, y_pred)

# Capture data in pandas dataframe

data = {'y_true': y_true, 'y_pred': y_pred}

# Assign to df

df = pd.DataFrame(data, columns=['y_true', 'y_pred'])

# Create the confusion matrix 

confusion_matrix = pd.crosstab(df['y_true'], df['y_pred'], rownames = ['Actual'], colnames=['Predicted'])

# Using seaborn, we can create a more vivid display of the matrix 
 
sn.heatmap(confusion_matrix, annot=True)
plt.title("Confusion Matrix BERT Deaths Set")
plt.show()
