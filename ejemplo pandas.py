"""
import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})

#Display the first three rows:
df.head(3)
#Obtain column  'a'
df['a']

#Find the unique values in column  'a' :

df['a'].unique()

#Return a dataframe with only the rows where column  a  is less than two:
df[df['a']<2]

"""