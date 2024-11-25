from dataframe import matrix
from dataframe import result_df
import numpy as np
import pandas as pd
def algorithm(result_df):
    #First create ratio of matrix. 
    #print(result_df)

    negatives_df = result_df.iloc[0, :].where(result_df.iloc[0, :] < 0) #This part I have yet to finish. Dont complete it. Do u think this is a good implementation? I saw u doing it in way less lines in a more efficient way. Is what im doing wrong to some extent?

    print(negatives_df)
    return negatives_df
algorithm(result_df)
help(np)