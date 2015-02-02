import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

loansdata = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv') #read in the Lending Club Data as a csv, store in loansdata
loansdata.dropna(inplace=True) #drop the missing data+

freq = collections.Counter(loansdata['Open.CREDIT.Lines'])
chi, p = stats.chisquare(freq.values())

print chi, p