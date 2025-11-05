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

def play_scb():
	global attempts, word_length, alphabet

	get_words()

	# Creates variables used for the game
	word_has_been_guessed = False
	mystery_word = select_random_word()
	attempts_left = attempts
	attempts_used = 0
	chophy_letters = []
	storts_letters = []
	bascat_letters = []
	unguessed_letters = alphabet

	while word_has_been_guessed == False and attempts_left > 0:
		print(f"You have {attempts_left} attempts remaining.")

		while True:
			try:
				# Displays letter group lists. 
				# The ", ".join(letters) syntax is used to remove brackets and quotation marks when printing the list
				print(f"\nChophy: {", ".join(chophy_letters)}")
				print(f"Storts: {", ".join(storts_letters)}")
				print(f"Bascat: {", ".join(bascat_letters)}")
				print(f"Unguessed: {", ".join(unguessed_letters)}\n")
				guess = input(f"Guess a {word_length} letter word: ")
			except ValueError:
				continue
			if not guess.isalpha():
				print("You must type in valid Alphabetical characters.\n")
			elif len(list(guess.strip())) != word_length:
				print(f"Word must be {word_length} letters long.\n")
			else:
				guess = guess.strip().lower()
				print()
				break

		attempts_used = attempts_used + 1

		# Ends game is user guessed correct word
		if mystery_word == guess:
			word_has_been_guessed = True
			break
		else:
			attempts_left = attempts_left - 1

			# Removes all guessed letters in this for loop. 
			# The letters then get added back to its appropiate list in the "Letter Checking" for loop
			for i in range(word_length):
				if guess[i] in chophy_letters:
					chophy_letters.remove(guess[i])
				elif guess[i] in storts_letters:
					storts_letters.remove(guess[i])
				elif guess[i] in bascat_letters:
					bascat_letters.remove(guess[i])
				elif guess[i] in unguessed_letters:
					unguessed_letters.remove(guess[i])

			# Letter Checking
			for i in range(word_length):
				if guess[i] in mystery_word and guess[i] == mystery_word[i]:
					print(f"{guess[i]}, Green / Chophy")
					chophy_letters.append(guess[i])
					continue
				if guess[i] in mystery_word:
					print(f"{guess[i]}, Yellow / Storts")
					storts_letters.append(guess[i])
				else:
					print(f"{guess[i]}, gRey / Bascat")
					bascat_letters.append(guess[i])

			# Removes duplicate letters from list
			chophy_letters = list(set(chophy_letters))
			storts_letters = list(set(storts_letters))
			bascat_letters = list(set(bascat_letters))

			# Sorts lists
			chophy_letters.sort()
			storts_letters.sort()
			bascat_letters.sort()

			print()

	# Game End
	if attempts_left == 0:
		print("You have 0 attempts left and lost the game.")
		print(f'The word was "{mystery_word}".')
	else: 
		print(f"Congratulations! You have successfully guessed the word!")
		print(f'The word was "{mystery_word}".')
		print(f"You guessed the word in {attempts_used} attempts.")

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

	# Lets user change the settings that they want to change.
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

def get_words():
	try:
		with open("assets/words_10k_most_common.txt", "r") as file:
			for word in file:
				# word.strip() function removes \n (New Line Character)
				if len(list(word.strip())) != word_length:
					continue
				word_list.append(word.strip()) 
	except FileNotFoundError:
		print("No File Exists")

def select_random_word():
	global word_list
	word = random.choice(word_list)
	return word

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

# Creates empty list to put words in
word_list = []

# Changeable settings for the game
word_length = 5
attempts = 6

# English Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if __name__ == "__main__":
	main()