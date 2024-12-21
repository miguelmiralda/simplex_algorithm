import pygame
import sys
import pandas as pd
import numpy as np

#This promp will make a dataframe. The first line is the function we are looking to optimize

class simplex_algorithm:
    def __init__(self, matrix):
        self.matrix = matrix
    def algorithm(self):
     
        global result_df
        Normal_constrains = self.matrix.iloc[:, :-1] # All columns except the inequality column
        #print(Normal_constrains)
        Inequality_constrain = self.matrix.iloc[:, -1:] #inequality columns

        num_slack_vars = self.matrix.shape[0]-1  # number of slack variables (rows - 1 function to optimize (first line))
        #print(num_slack_vars)
    
        #  Create an identity matrix with the number of rows equal to constraints_df
        num_rows = len(self.matrix)
        #print(num_rows)

        identity_matrix = np.zeros((num_rows, num_slack_vars)) #Zero matrix with the desired dimensions

        identity_matrix[1:, :] = np.identity(num_rows - 1) #Assign an identity matrix starting on the values of the zero matrix I want to start from:

        #print(identity_matrix)
    
        slack_columns = [f"S{i+1}" for i in range(num_slack_vars)] #Creates S columns
        slack_variables_df = pd.DataFrame(identity_matrix, columns=slack_columns) #Slack df

        #print(slack_variables_df) 
        #print(num_slack_vars)
        almost_result_df = pd.concat([Normal_constrains, slack_variables_df], axis=1) # Creates df consisting of constrains + slack variables
    
        result_df = pd.concat([almost_result_df, Inequality_constrain], axis=1) # Joins earlier df with inequality constrain
    
        result_df.iloc[0, :] = result_df.iloc[0, :]*-1 #If you don't want the negative 0s, use this instead: .apply(lambda x: -x if x != 0 else 0)

        #Now gonna select the more negative value in the function to optimize
        Key_value = min(result_df.iloc[0, :])

        array_with_index = result_df.reset_index().to_numpy()   #reset index to use np.where
  
        Key_column = np.where(array_with_index[0,:] == Key_value)    # np.where works by finding the index of the key value in that row
    
        print(Key_column)

        #print(result_df)
        return result_df
        #algorithm(Dataframe_1)

constrains_df_1 = pd.DataFrame({'x1': [1, 2,3,1],'x2': [4, 1, 5,3], "<=": [0,3,9,5]})
constrains_df_2 = pd.DataFrame({'x1': [2, 3,4,2],'x2': [3, 0, 4,2], "<=": [0,3,9,5]}) #This one I made up, so idk if it can be maximized 

Dataframe_1 = simplex_algorithm(constrains_df_1)
Dataframe_2 = simplex_algorithm(constrains_df_2)
print(Dataframe_1.algorithm())