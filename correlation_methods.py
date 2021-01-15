'''
Following are 3 methods to find correlation between numerical parameters:
1. Covariance
2. Pearson's Covariance
3. Spearman's covariance

Here keep in mind the variables should be numerical data ONLY and not categorical.

For more theory knowledge about these three methods referee the link below:
https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
'''

import numpy as np #used to import mathematical operations
import matplotlib.pyplot as plt #used to plot different things in python
import pandas as pd
from numpy import mean
from numpy import std
from scipy import stats

dataset = pd.read_csv('file_name.csv')
dataset[0:4]

#consider two parameters between whom you want to find a relation.
data1 = dataset.col1
data2 = dataset.col2

# METHOD 1: Covariance

print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
# plot
plt.scatter(data1, data2)
plt.show()

#Higher the numer higher the correlation amongst two parameters
#Consider the diagonal values for the same
covariance = np.cov(data1, data2)


# METHOD 2: Pearson's Covariance
#To be used if we know there is some gaussian or gaussian like distribution
#Gives more precision than covariance and easy to understand.

#value between -0.5 to 0.5 means no strong correlation 
from scipy.stats import pearsonr
corr, _ = pearsonr(data1, data2)
print(corr)



# METHOD 3: Spearman's covariance
#Can be used if we do not know if it is Gaussian and Non-Gaussian distribution.

#value between -0.5 to 0.5 means no strong correlation
from scipy.stats import spearmanr
corr, _ = spearmanr(data1, data2)
print(corr)
