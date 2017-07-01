from random import randint

def welcome():
	'''This welcome message gets the player's name'''
	player_name = input("\nWelcome to Math Quiz 1.0! What is your name? ")
	return player_name

def difficulty(player_name):
	'''This will prompt the player for a difficulty level from 1-10'''
	difficulty_level = input("\nHi " + player_name.title() + "! What difficulty "
		"level would you like for this quiz (1-10)? ")
	while (int(difficulty_level) < 1) or (int(difficulty_level) > 10):
		difficulty_level = input("\nI said 1-10! What level would you like? ")
	return difficulty_level

def play_game(player_name, difficulty_level):
	# Start the right/wrong answer counters at 0
	total_right = 0
	total_wrong = 0

	while True:
		# Create random numbers based on difficulty level
		num1 = randint(1,(5 * int(difficulty_level)))
		num2 = randint(1,(5 * int(difficulty_level)))

		# Difficulty 1 is only + and -, 10 is only x and /
		if int(difficulty_level) == 1:
			rand_op = randint(1,2)
		elif int(difficulty_level) == 10:
			rand_op = randint(3,4)
		else:
			rand_op = randint(1,4)
		
		# Get math result and ask for player's guess
		if rand_op == 1:
			result = num1 + num2
			guess = input('\n' + str(num1) + ' + ' + str(num2) + ' = ')
		elif rand_op == 2:
			result = num1 - num2
			guess = input('\n' + str(num1) + ' - ' + str(num2) + ' = ')
		elif rand_op == 3:
			result = num1 * num2
			guess = input('\n' + str(num1) + ' x ' + str(num2) + ' = ')
		else:
			num1 = num1 * num2
			result = int(num1 / num2)
			guess = input('\n' + str(num1) + ' / ' + str(num2) + ' = ')

		# Did the player guess correctly?
		if not guess:
			total_wrong += 1
			print("You forgot to guess! The answer was " + str(result) + ".")
		elif guess.lower() == 'q':
			total_questions = total_right + total_wrong
			print("\nThanks for playing, " + player_name.title() + "."
				"\nYour results: " + str(total_right) + "/"
				+ str(total_questions) + "\n")
			break
		elif int(guess) == result:
			total_right += 1
			print("Yes, that is correct!")
		else:
			total_wrong += 1
			print("Sorry, the correct answer was " + str(result) + ".")