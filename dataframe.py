import pygame
import sys
import pandas as pd
import numpy as np

#def simplex_algorithm(matrix):
    #try:
        # Attempt to convert the input to a number and multiply by 2
        #result = float(input_text) * 2
        #return f"Processed Result: {result}"
    #except ValueError:
        # Handle non-numeric input
        #return "Please enter a valid number."


# I am trying to create a matrix to perfom simplex algorithm. I create it row by row

counter_for_creating_df = 0 # This decides whether we create the dataframe or not. ONLY the first value inputed will decide it becaouse after that, the counter will go up

# To create the specific dataframe, I need to first know the number of columns (x1, x2, x3, x4)
# Therefore the first answer will be a number from 1 to 4, that decides the number of columns

#Very important to add a callback. If not for this part of the code (and the main part), The dataset wouldn't form
def dataframe_creation(input_text, callback=None):
    global df 
    num_columns = int(input_text)  # Convert input_text to an integer
    possible_columns = ['x1', 'x2', 'x3', 'x4']
    global counter_for_creating_df
    global df_columns
    if counter_for_creating_df == 0:
        columns_used = possible_columns[:num_columns]
        df_columns = pd.DataFrame(columns= columns_used)
        counter_for_creating_df +=1
        print(df_columns)
        if callback:
            callback(df_columns)
        return df_columns
    else:
        return "already formed a dataset"
                

row_index = 0  # This will be our row counter
column_index = 0


def save_answer_to_df(answer):

    global answers_df
    global row_index # Use the global counter for the row index
    global column_index # Use the global counter for the column index
    # Save the answer to the DataFrame at the current index
    answers_df.iloc[row_index , column_index] = answer
    column_index += 1  # Increment index for the next answer
    print("df:" , answers_df) # I want to keep track on the changes on the dataframe, but it doesn't seem to be working. Help me out. It's not printing anything on the terminal
    if answer == "change":
        row_index += 1
        column_index = 0


constrains_df = pd.DataFrame({'x1': [1, 2,3,1],'x2': [4, 1, 5,3], "<=": [0,3,9,5]})

def matrix(constrains_df):
     
    global result_df
    Normal_constrains = constrains_df.iloc[:, :-1] # All columns except the inequality column
    #print(Normal_constrains)
    Inequality_constrain = constrains_df.iloc[:, -1:] #inequality columns

    num_slack_vars = constrains_df.shape[0]-1  # number of slack variables (rows - 1 function to optimize (first line))
    #print(num_slack_vars)
    
     #  Create an identity matrix with the number of rows equal to constraints_df
    num_rows = len(constrains_df)
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
    
    print(result_df)
    return result_df
matrix(constrains_df)