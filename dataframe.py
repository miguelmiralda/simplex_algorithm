import pygame
import sys
import pandas as pd
import numpy as np

# I am trying to create a matrix to perfom simplex algorithm. I create it row by row

counter_for_creating_df = 0 # This decides whether we create the dataframe or not. ONLY the first value inputed will decide it becaouse after that, the counter will go up

# To create the specific dataframe, I need to first know the number of columns (x1, x2, x3, x4)
# Therefore the first answer will be a number from 1 to 4, that decides the number of columns

#Very important to add a callback. If not for this part of the code (and the main part), The dataset wouldn't form. This is only relevant for the pygame implementation
#It isn't relevant for the actual_algorithm snippet, which is the only real working part for now
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

#The idea of this part was to create a window pop up where you filled the number of columns the df has, and afterwards you input the values, 
#That would subsequently be saved in a df and redirected to the algorithm. Obviously this part turned out more complicated than expected, Will have to 
#Search for a better library to work with other than pygame for the display window!
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