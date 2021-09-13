# Imports

import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import pandas as pd
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.metrics import roc_auc_score

# Function to plot two curves

def plot_roc_curve(fpr, tpr, fpr2, tpr2):
    plt.plot(fpr, tpr, color='orange', label='ROC Pharma Set')
    plt.plot(fpr2, tpr2, color='blue', label='ROC Death Set')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve Training Set')
    plt.legend()
    plt.show()

# Readin Dataset

df = pd.read_csv('Summer_Project/twint/vaccine_pharma_set_5Jul.csv')
df2 = pd.read_csv('Summer_Project/twint/vaccine_deaths_set_25June.csv')

# Find FPR & TPR, Plot ROC Curve

y_true = np.array(df['Conspiracy'])
y_scores = np.array(df['sentence_transformers_exp'])

y_true2 = np.array(df2['Conspiracy.1'])
y_scores2 = np.array(df2['sentence_transformers_death'])

fpr, tpr, thresholds = roc_curve(y_true, y_scores)
fpr2, tpr2, thresholds2 = roc_curve(y_true2, y_scores2)

plot_roc_curve(fpr, tpr, fpr2, tpr2)
