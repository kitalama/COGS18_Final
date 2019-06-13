"""A collection of functions for my project."""

import string
import random

pos_list = ['Yes','yes','sure','ok','yeah','ya','fine']
neg_list = ['no', 'nope', 'nah']

def user_input():
    """Take an input from the user and determine whether they want to play.

    Parameters

    ----------

    msg : string

        Form of agreement (yes) or disagreement (no) from the user

    Returns

    -------

    output : string

        String containing a phrase depending on what the user chose

    """
    
    # The initial input message given when you run the chat
    msg = input('Hello! Want to play a game of rock, paper, scissors!?\t')
    
    if msg in pos_list:
        output = 'Okay, you pick first!'
        return output
    
    if msg in neg_list:
        output = input("C'mon! Let's play a game of rock, paper, scissors!\t")
        return output, user_input() # Returns user back to the beginning and asks them to play again
    
    else:
        output = input("Sorry, I don't understand. Try again.\t")
        return output, user_input() # Returns user back to the beginning and asks them to play again

    
def user_option():
    """Checks that input from user is either rock, paper, or scissors.

    Parameters

    ----------

    user_choice : string

        Check if input from user is rock, paper, or scissors

    Returns

    -------

    output : string

        Identify word user selected or if it is not understandable, ask to type it again

    """
        
    user_choice = input('Okay, you pick first!  Choose between rock, paper, scissors: ')
    
    if user_choice in ['Rock', 'rock', 'R', 'r']:
        user_choice = 'rock'
        return user_choice
        
    elif user_choice in ['Paper', 'paper', 'P', 'p']:
        user_choice = 'paper'
        return user_choice
        
    elif user_choice in ['Scissors', 'scissors', 'S', 's']:
        user_choice = 'scissors'
        return user_choice
        
    else: # If user does not select any of the following, the will be asked to try again
        user_choice = "Sorry, I don't understand. Try again."
        return user_choice
        user_option() # This will take them to the beginning to try again
        
        
def comp_option():
    """Computer will generate a random word: rock, paper, scissors

    Parameters

    ----------

    comp_choice : int

        Computer chooses random integer that is assigned to rock, paper, or scissors

    Returns

    -------

    output : string

        String containing a phrase depending on what computer chose

    """
    
    comp_choice = random.randint(1,3)
    
    if comp_choice == 1: # Assigns 'rock' to the value of 1
        comp_choice = 'rock'
        print('My turn! I chose rock.')
    
    elif comp_choice == 2:
        comp_choice = 'paper' # Assigns 'paper' to the value of 2
        print('My turn! I chose paper.')
        
    elif comp_choice == 3:
        comp_choice = 'scissors' # Assigns 'scissors' to the value of 3
        print('My turn! I chose scissors.')
        
    return comp_choice


def evaluate(user_choice, comp_choice):   
    """Return a response that reveals if the user won or not

    Parameters

    ----------

    user_choice : string

        Check if input from user is rock, paper, or scissors
    
    comp_choice : string
    
        Choose random integer that is assigned to rock, paper, or scissors

    Returns

    -------

    output : string

        String containing a phrase stating whether computer or user won

    """
    
    if user_choice == comp_choice:
        output = "It's a tie."
        return output
    
    elif user_choice == 'rock' and comp_choice == 'scissors':
        output = "You won!"
        return output
        
    elif user_choice == 'rock' and comp_choice == 'paper':
        output = "Sorry, maybe better luck next time."
        return output
    
    elif user_choice == 'paper' and comp_choice == 'rock':
        output = "You won! Nice one!"
        return output
    
    elif user_choice == 'paper' and comp_choice == 'scissors':
        output = "Sorry, you lost."
        return output
    
    elif user_choice == 'scissors' and comp_choice == 'rock':
        output = "Sorry, gotcha there."
        return output
    
    elif user_choice == 'scissors' and comp_choice == 'paper':
        output = "Great job! You won!"
        return output 
    
    
def end_chat():
    """Checks to see if user wants to end the chat

    Parameters

    ----------

    user_quit : string

        User decides whether to end chat

    Returns

    -------
        
    user_option : function
    
        Takes the user back to the beginning to start the chat over again
        
    output : string

        String with a phrase that ends the chat
        
    user_quit
    
        If input cannot be determined, takes the user back to the beginning of the end_chat function 

    """     
    
    chat = True
    while chat: 
        
        user_quit = input("Do you want to play again? ('yes' or 'no')\t")

        if user_quit == 'yes':
            return user_option # Takes the user back to the beginning of the chat
        
        elif user_quit == 'no':
            output = print('Thanks for playing!')
            return output # Ends the game with a phrase
            
            break
            
        else:
            output = input("Sorry, I don't understand. Try again.\t")
            return output, user_quit # Takes the user back to the beginning of the function to try again
