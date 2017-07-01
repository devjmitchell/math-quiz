'''
I was showing my daughter, Julia, that you can create anything you want if you
know how to code... We were talking about a simple 'math game', so I decided to
spend a little over an hour (I know, but I'm brand new!) making this one.

P.S. I've made a few modifications since the first pass, so I've probably spent
a few hours now.
'''

from quiz_functions import *

player_name = welcome()
difficulty_level = difficulty(player_name)
print("\nOkay, level " + difficulty_level + "! Answer the following questions."
	"\n(type 'q' when you'd like to quit playing)")
play_game(player_name, difficulty_level)