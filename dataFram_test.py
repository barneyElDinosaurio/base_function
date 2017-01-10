import numpy as np
import pandas as pd

def df_practice():
    a=[1,-23,4,5,6,7,-4,34,3,5,33]
    b=[-2,55,-5,99,3,-3,55,3,-1,4,7]
    df=pd.DataFrame({'A':a,'B':b})
    print df
    #df.loc[(df['A']>0) & (df['B']<0),'A']=100
    df.ix[(df['A']>0) & (df['B']<0),'A']=100
    print df

df_practice()