import statsmodels.formula.api as smf
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import scipy.stats as stats
import pylab
data_path = "airline_2m.csv"
#CSV Can be directly downloaded as a tar file here: 

#https://dax-cdn.cdn.appdomain.cloud/dax-airline/1.0.1/airline_2m.tar.gz?_ga=2.241493383.460169643.1645306071-17791737.1643504108

# Credit to IBM's Airline Dataset for the data and encoding code.


data = pd.read_csv(data_path, encoding = "ISO-8859-1",
                 dtype={'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str})
#Code Provided By IBMs Airline Reporting Carrier on-time performance set. 
#This helps python better interpret the data frame because it is not encoded in UTF-8 
#An alternative to this could be to actually change the file to be encoded in UTF-8
#but this was difficult to do with how big the file was.

sample = data.sample(10000)
#Create Sample For Examples


def originDelays(df, orig, desto):
    """
    This Function Takes in a dataframe from the Airline Dataset. 
    Then the Data is isolated strictly to the 1 dimensional frame of Arrival
    Delays for flights from one airport (IATA location ID) to another airport (" ").
    
    The arguments follow this format:
    
    originDelays(dataframe,originIATA,destIATA)
    
    
    """
    originSubset = df[df['Origin'] == orig]
    originSubset = originSubset[originSubset['Dest'] == desto ]
    #Shaves the DataFrame so that we are just looking at origin rows
    #Then cuts out desired destinations.
    
    print(originSubset['Origin'])
    #Print Statement To verify the Origin
    print(originSubset['Dest'])
    #Print Statement to verify the Destination

    arvl_delay = originSubset['ArrDelay'].fillna(0)
    #Takes out the Arrival Delay column, adds 0 for the NA spots 
    #NA spots infer no delay from IBMs Dataset
    
    qData = arvl_delay
    #Rename for sake of callability
    
    plt.hist(arvl_delay, bins='auto')
    #Constructs the histogram with automatic sizing
    plt.xlabel('Delay')
    #Delay in Minutes
    plt.ylabel('Frequency')
    #Plot a histogram for verification of data
    plt.show()
    
    print(stats.describe(qData))
    #Descriptive statistics to compare with Histogram
    
    sm.qqplot(qData, stats.norm, fit=True,line ='45', color ='r')
    #The Normal Distribution Q-Q Plot
    
    sm.qqplot(qData, stats.skewnorm, fit=True,line ='45', color='b')
    #The Skewed Normal Distribution Q-Q Plot
    
    sm.qqplot(qData, stats.lognorm, fit=True,line ='45', color = 'y')
    #The LogNormal Distribution Q-Q Plot
    
    sm.qqplot(qData, stats.expon, fit=True,line ='45', color='g')
    #The Exponential Distribution Q-Q Plot
    
    plt.show()


def plotter(dataFrame, xColumn, yColumn):
    """
    This function takes in a dataframe, and two column names to 
    compare in a scatter plot.
    The arguments follow this format:
    plotter(dataframe, x column name, y column name) 
    
    """
    x = dataFrame[xColumn]
    y = dataFrame[yColumn]
    #Renamed x and y for clarity in scatter call
    
    plt.scatter(x,y)
    #Construct the scatter plot
    
plotter(sample,'AirTime','Distance')
#Example Call of Plotter


def ols_model(df,x, y):
    """
    This Function takes in a dataframe and two columns of that 
    data frame to create a ordinary least squares regression
    """
    regression = smf.ols(formula = 'y ~ x', data = df).fit()
    #Performs an Ordinary Least Squares Regression
    
    summary = regression.summary()
    print(summary)
    return 
  
ols_model(sample, sample['ArrDelay'],sample['Distance'])
#Example Call ols_model

