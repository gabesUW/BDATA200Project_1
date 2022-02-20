#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import scipy.stats as stats
import pylab
data_path = "airline_2m.csv"
data = pd.read_csv(data_path, encoding = "ISO-8859-1",
                 dtype={'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str})
# Credit to IBM's Airline Dataset for the data and encoding code.


# In[77]:


sample = data.sample(10000)


def originDelays(df, orig, desto):
    """
    (dataframe,originIATA,destIATA)
    
    
    """
    originSubset = df[df['Origin'] == orig]
    originSubset = originSubset[originSubset['Dest'] == desto ]
    #Shaves the DataFrame so that we are just looking at origin rows
    #Then cuts out desired destinations.

    
    
    print(originSubset['Origin'])
    print(originSubset['Dest'])
    #Print Statement To verify the Origin
    #Print Statement to verify the Destination
    

    arvl_delay = originSubset['ArrDelay'].fillna(0)
    #Takes out the Arrival Delay column, adds 0 for the NA spots 
    #NA spots infer no delay from IBMs Dataset
    
    qData = arvl_delay
    #Rename for sake of clarity
    
    plt.hist(arvl_delay, bins='auto')
    plt.xlabel('Delay')
    plt.ylabel('Frequency')
    #Plot a histogram for verification of data
    plt.show()
    
    print(stats.describe(qData))
    #
    
    sm.qqplot(qData, stats.norm, fit=True,line ='45', color ='r')
    sm.qqplot(qData, stats.skewnorm, fit=True,line ='45', color='b')
    sm.qqplot(qData, stats.lognorm, fit=True,line ='45', color = 'y')
    sm.qqplot(qData, stats.expon, fit=True,line ='45', color='g')
    plt.show()

originDelays(data, 'LAX', 'DFW' )  


# In[50]:


stats.kstest(duh, stats.lognorm.cdf, args=(1,100),N=20)


# In[82]:


def plotter(dataFrame, xColumn, yColumn):
    x = dataFrame[xColumn]
    y = dataFrame[yColumn]
    plt.scatter(x,y)
plotter(sample,'AirTime','Distance')


# In[56]:


def simple_model(x, y):
    model = smf.ols(formula = 'y ~ x', data = df)
    results = model.fit()
    summary = results.summary()
    print(summary)
    return 
simple_model(sample['ArrDelay'],sample['Distance'])

