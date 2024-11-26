import pygame
import sys
import pandas as pd
import numpy as np
from simplex_algorithm.dataframe import dataframe_creation

display_result = False  # Flag to control result rendering
df_columns = ""  # Store the DataFrame columns as a string

def interactive_display(width=800, height=600):
    global display_result, df_columns  # Ensure we use the global variables

    # Initialize Pygame
    pygame.init()
    
    # Set up display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Interactive Display")
    
    # Set up fonts and colors
    font = pygame.font.Font(None, 74)
    input_text = ""
    text_color = (255, 255, 255)  # White
    background_color = (0, 0, 0)  # Black
    
    # Callback function to update the display result
    def update_display_result(df):
        global display_result, df_columns
        df_columns = ', '.join(df.columns)  # Convert DataFrame columns to a string
        display_result = True  # Signal that the result is ready to display

    # Main loop
    running = True
    while running:
        screen.fill(background_color)
        
        # Capture events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Process the input_text and store the result
                    try:
                        display_result = False  # Reset display flag
                        dataframe_creation(input_text, callback=update_display_result)  # Pass callback
                    except ValueError:
                        print("Please enter a valid integer.")

                    input_text = ""  # Clear text after processing
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Remove last character
                else:
                    input_text += event.unicode  # Add the typed character
        
        # Render the current input text on screen
        input_surface = font.render(str(input_text), True, text_color)
        screen.blit(input_surface, (50, 50))
        
        # Render the result text on screen if display_result is True
        if display_result:
            result_surface = font.render(str(df_columns), True, text_color)
            screen.blit(result_surface, (50, 150))
        
        pygame.display.flip()

    # Exit Pygame
    pygame.quit()
    sys.exit()

# Call the function
interactive_display()
