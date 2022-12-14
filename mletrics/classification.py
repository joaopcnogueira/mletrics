# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_classification.ipynb.

# %% auto 0
__all__ = ['ks']

# %% ../nbs/02_classification.ipynb 3
import pandas as pd
from numpy import ndarray
from scipy.stats import ks_2samp

def ks(y_true: ndarray,    # the target variable, contains 0's and 1's
       y_prob: ndarray):   # the probability of the

   df = pd.DataFrame({
      'target': y_true,
      'probability': y_prob
   })

   class0 = df[df['target'] == 0]
   class1 = df[df['target'] == 1]

   return ks_2samp(class0['probability'], class1['probability']).statistic
