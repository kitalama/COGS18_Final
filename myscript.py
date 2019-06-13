"""Script to run some part of my project."""

import sys
sys.path.append('../')

from my_module.myfunctions import user_input, user_option, comp_option, evaluate(user_choice, comp_choice), end_chat


def main_game():
    """Main function to run chatbot"""
    
    chat = True
    while chat: 
            
        # Gets input message from the user and assigns it as out_msg
        out_msg = user_input()
        
        # Allows user to select either 'rock', 'paper', or 'scissors' and assign it as user_choice.
        user_choice = user_option()
        
        print('')
        
        # Computer will generate a random word from 'rock', 'paper', or 'scissors' and assign it as comp_choice.
        comp_choice = comp_option()
        
        print('')
        
        # Evaluates whether the computer or user wins.
        out_msg = evaluate(user_choice, comp_choice)
        print(evaluate(user_choice, comp_choice))

        print('')
        
        # Ask if user wants to continue playing.
        user_quit = end_chat()