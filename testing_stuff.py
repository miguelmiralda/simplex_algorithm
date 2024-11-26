import pandas as pd

practice_df = pd.DataFrame({'x1': [1, 2,3,1],'x2': [4, 1, 5,3], "x3": [0,3,9,5], 'x4': [1,2,3,4]})
print(practice_df.iloc[0, :-1]) 



import numpy as np
import pandas as pd

# Sample constraints dataframe
constraints_df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

# Number of slack variables
num_slack_vars = constraints_df.shape[0] - 1  # rows - 1 (function to optimize)

# Create an identity matrix with the number of rows equal to constraints_df
num_rows = len(constraints_df)
print(num_rows)

identity_matrix = np.zeros((num_rows, num_slack_vars))

# Set the first 1 in the first column of the second row
identity_matrix[1:, :] = np.identity(num_rows - 1)

print("Modified Identity Matrix:")
print(identity_matrix)

