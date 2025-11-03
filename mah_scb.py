import random

word_list = []
word_length = 5

def main():
	get_words()
	# print(word_list)

	random_word = random.choice(word_list)

	while True:
		try:
			desired_letter = input("Input your desired letter: ")
			print()
		except ValueError:
			print("Skibidi Toilet")
			continue
		if len(list(desired_letter)) != 1:
			print("You must type in ONE valid Alphabetical character.")
			print()
		elif not desired_letter.isalpha():
			print("You must type in a valid Alphabetical character.")
			print()
		else:
			desired_letter = desired_letter.lower()
			break
	
	if desired_letter in random_word:
		print("Yes")
		print(f"{desired_letter} is in {random_word}")
		print(f"Position: {random_word.index(desired_letter)}")
	else:
		print("No")
		print(f"{desired_letter} is not in {random_word}")

	print()

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

if __name__ == "__main__":
	main()