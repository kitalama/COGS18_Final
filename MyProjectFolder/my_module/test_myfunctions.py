"""Test for my functions."""

from myfunctions import evaluate(user_choice, comp_choice)

    
def test_evaluate(user_choice, comp_choice):
    assert evaluate('rock', 'paper') == 'Sorry, maybe better luck next time.'
    assert evaluate('scissors', 'paper') == 'Great job! You won!'
    assert evaluate('rock', 'rock') == "It's a tie!"
