import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import statistics
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score

# Reading in datasets

df = pd.read_csv('Name')
y_true = df['Column Name']
y_pred = df['Column Name']

# Check the arrays that you are entering into the curve

precision, recall, thresholds = precision_recall_curve(y_true, y_pred)

# Plot the Precision-Recall Graph

y = precision
x = recall

plt.title("Name")
plt.xlabel("Recall")
plt.ylabel("Precision")
Name , = plt.plot(x, y, color = 'blue')

# Ledgend used to plot graphs
plt.legend([Name], ['Name'])
