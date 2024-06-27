# Modules
import random
import termcolor
import pyfiglet
import os

print(termcolor.colored(pyfiglet.figlet_format("Guess the number"), color='light_green'))

def play_game(level):
	if level == 1:
		min_num, max_num = 1, 10
		attempts = 3
	elif level == 2:
		min_num, max_num = 1, 50
		attempts = 6
	elif level == 3:
		min_num, max_num = 1, 100
		attempts = 9
	else:
		print(termcolor.colored("Invalid level. please choose 1, 2 or 3.", color='red'))
		return

	secret_number = random.randint(min_num, max_num)

	print(termcolor.colored(f"Welcome to level {level}! Guess the number between {min_num} and {max_num}", color= 'yellow'))

	while attempts > 0:
		guess = int(input(termcolor.colored(f"Attemps {attempts}: Enter your guess:", color="light_green")))
		if guess == secret_number:
			os.system('cls')
			print(termcolor.colored(pyfiglet.figlet_format("Winer"), color='green'))
			print(termcolor.colored("Congratulations! You guessed it right!", color='green'))
			break
		elif guess < secret_number:
			print(termcolor.colored("Try a higher number.", color='light_red'))
		else:
			print(termcolor.colored("Try a lower number.", color='light_blue'))
		attempts -= 1
	
	if attempts == 0:
		os.system("cls")
		print(termcolor.colored(pyfiglet.figlet_format("Loser"), color='red'))
		print(termcolor.colored(f"Sorry, you're out of attempts. The secret number was {secret_number}.", color='red'))


try:
	level_choice = int(input("Choose a level 1, 2 or 3: "))
	play_game(level_choice)
except ValueError:
	print(termcolor.colored("Invalid input. Please enter a valid level (1, 2, or 3).", color='red'))