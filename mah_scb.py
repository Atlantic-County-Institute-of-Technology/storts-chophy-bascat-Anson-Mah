import random
import os

def main():
	while True:
		# Initial Menu
		print("-------------------------")
		print("[0]. Quit Program")
		print('[1]. Play "Storts, Chophy, Bascat"')
		print("[2]. View Settings")
		print("[3]. Change Settings")
		print("[8]. 3rd of November")

		# Input Correction
		# If the user's input would break the program, it changes the input such that it will not break the program.
		while True:
			try:
				selection = int(input("Select an Option: "))
				break
			except ValueError:
				# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
				selection = 9
				break

		clear_terminal()

		# Runs different functions based off of what you inputted
		match selection:
			case 0:
				print("Program Terminated")
				exit()
			case 1:
				play_scb()
			case 2:
				view_settings()
			case 3:
				change_settings()
			case 8:
				november_3()

def play_scb():
	print("Skibidi!!!!!")

def view_settings():
	global word_length, attempts
	print("Current Settings")
	print("-----------------")
	print(f"Word Length: {word_length}")
	print(f"Amount of Attempts: {attempts}")

def change_settings():
	# Settings Menu
	print("Which settings would you like to change?")
	print("-----------------------------------------")
	print("[1]. Word Length")
	print("[2]. # of Attempts")

	# Input Correction
	# If the user's input would break the program, it changes the input such that it will not break the program.
	while True:
		try:
			selection = int(input("\nSelect an Option: "))
			break
		except ValueError:
			# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
			selection = 9
			break

	match selection:
		case 1:
			# Input Validation
			# Only allows positive integers
			while True:
				try:
					user_word_length = int(input("\nInput your desired word length: "))
				except ValueError:
					print("\nPlease input a positive integer.\n")
					continue
				if user_word_length <= 0:
					print("\nYou have inputted a non-positive integer. Please input a positive integer.\n")
				else:
					global word_length
					word_length = user_word_length
					print(f"\nWord Length set to {word_length}")
					break
		case 2:
			# Input Validation
			# Only allows positive integers
			while True:
				try:
					user_attempts = int(input("\nInput your desired amount of attempts: "))
				except ValueError:
					print("\nPlease input a positive integer.\n")
					continue
				if user_attempts <= 0:
					print("\nYou have inputted a non-positive integer. Please input a positive integer.\n")
				else:
					global attempts
					attempts = user_attempts
					print(f"\nAmount of attempts set to {attempts}")
					break
		case _:
			# Brings you back to the Settings Menu
			clear_terminal()
			change_settings()

def november_3():
	get_words()

	random_word = random.choice(word_list)

	while True:
		try:
			desired_letter = input("Input your desired letter: ")
			print()
		except ValueError:
			print("Skibidi Toilet")
			continue
		if len(list(desired_letter)) != 1:
			print("You must type in ONE valid Alphabetical character.\n")
		elif not desired_letter.isalpha():
			print("You must type in a valid Alphabetical character.\n")
		else:
			desired_letter = desired_letter.lower()
			break
	
	if desired_letter in random_word:
		print(f"Yes. {desired_letter} is in {random_word}")
		print(f"Position: {random_word.index(desired_letter)}")
	else:
		print(f"No. {desired_letter} is not in {random_word}")

def get_words():
	try:
		with open("assets/words_alpha.txt", "r") as file:
			for word in file:
				# word.strip() removes \n (New Line Character)
				if len(list(word.strip())) != word_length:
					continue
				word_list.append(word.strip()) 
	except FileNotFoundError:
		print("No File Exists")

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

# Creates empty list to put words in
word_list = []

# Changeable settings for the game
word_length = 5
attempts = 6

if __name__ == "__main__":
	main()