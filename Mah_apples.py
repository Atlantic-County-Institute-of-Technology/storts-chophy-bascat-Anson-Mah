# Name: Anson Mah
# Date: September 2025

import time

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##                                   ASSESSMENT                                  ##
## 5/5 - Read Input from the terminal for a quantity of apples                   ##
## 5/5 - Process the input with options                                          ##
## 5/5 - Create a product based on the chosen amount,                            ##
##       then return any whole or partial apples remaining.                      ##
## 5/5 - Loop until depletion, with an option for the user to refill the supply. ##
## 5/5 - Input Validation, prevent actions that                                  ##
##       would result in errors/unexpected behavior.                             ##
##                                                                               ##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##


def main():
	while True:

		time.sleep(1)
		print("")

		# Initial Menu
		print("[0]. Quit Program")
		print("[1]. Make Food")
		print("[2]. Add more Apples")
		print("[3]. View Recipe Costs")
		print("[4]. View Inventory")
	
		print("")
		# Input Correction
		# If the user's input would break the program, it changes the input such that it will not break the program.
		while True:
			try:
				selection = int(input("Select an Option: "))
				print("")
				break
			except ValueError:
				# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
				selection = 9
				break

		# Runs different functions based off of what you inputted
		match selection:
			case 0:
				print("Program Terminated")
				print("")
				exit()
			case 1:
				make_food()
			case 2:
				add_apples()
			case 3:
				show_recipes()
			case 4:
				show_inventory()

def make_food():
	# Food Menu
	print("[1]. Apple Pie")
	print("[2]. Apple Dumpling")
	print("[3]. Baked Apple")
	print("[4]. Apple Jam")
	print("[5]. Candy Apple")
	print("[6]. Apple Crumble")

	print("")
	# Input Correction
	# If the user's input would break the program, it changes the input such that it will not break the program.
	while True:
		try:
			desired_food = int(input("Select the food you wish to make: "))
			break
		except ValueError:
			# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the food menu
			desired_food = 9
			break
	print("")

	# Selects the appropiate food with its associated cost.
	match desired_food:
		case 1:
			food = "Apple Pie"
			cost = 4
		case 2:
			food = "Apple Dumpling"
			cost = 3.25
		case 3:
			food = "Baked Apple"
			cost = 3
		case 4:
			food = "Apple Jam"
			cost = 2.5
		case 5:
			food = "Candy Apple"
			cost = 2
		case 6:
			food = "Apple Crumble"
			cost = 1.75
		case _:
			# Brings you back to the Food Menu
			make_food()
	
	global apples_remaining
	print(f"One {food} requires {cost} Apples. You currently have {apples_remaining} Apples.")
	time.sleep(1)

	print("")

	# Input Validation
	# Only allows numbers greater than or equal to zero
	while True:
		try:
			amount_of_food = float(input(f"Input the amount of {food} you want to make: "))
		except ValueError:
			print("")
			print("Please input a positive number.")
			time.sleep(1)
			print("")
			continue
		if amount_of_food < 0:
			print("")
			print(f"You can only make a positive amount of {food}s.")
			time.sleep(1)
			print("")
		else:
			print("")
			break

	# If cost to make food is greater than apples remaining, do not make food. 
	# Else, make the desired amount of food.
	if cost * amount_of_food > apples_remaining:
		print("You too few apple!!! Make more apple!!!")
	else:
		print(f"Making {amount_of_food} {food}...")
		time.sleep(1)
		apples_remaining = apples_remaining - (cost * amount_of_food)
		print("")

		# Changes the appropiate food variable based off of what food you made.
		match food:
			case "Apple Pie":
				global apple_pies
				apple_pies = apple_pies + amount_of_food
				print(f"You have made {amount_of_food} {food}. You now have {apple_pies} {food} and {apples_remaining} Apples remaining.")
			case "Apple Dumpling":
				global apple_dumpling
				apple_dumpling = apple_dumpling + amount_of_food
				print(f"You have made {amount_of_food} {food}. You now have {apple_dumpling} {food} and {apples_remaining} Apples remaining.")
			case "Baked Apple":
				global baked_apple
				baked_apple = baked_apple + amount_of_food
				print(f"You have made {amount_of_food} {food}. You now have {baked_apple} {food} and {apples_remaining} Apples remaining.")
			case "Apple Jam":
				global apple_jam
				apple_jam = apple_jam + amount_of_food
				print(f"You have made {amount_of_food} {food}. You now have {apple_jam} {food} and {apples_remaining} Apples remaining.")
			case "Candy Apple":
				global candy_apple
				candy_apple = candy_apple + amount_of_food
				print(f"You have made {amount_of_food} {food}. You now have {candy_apple} {food} and {apples_remaining} Apples remaining.")
			case "Apple Crumble":
				global apple_crumble
				apple_crumble = apple_crumble + amount_of_food
				print(f"You have made {amount_of_food} {food}. You now have {apple_crumble} {food} and {apples_remaining} Apples remaining.")

# Lets user add more apples to their inventory
def add_apples():

	# Input Validation
	# Only allows numbers greater than or equal to zero
	while True:
		try:
			apples_to_add = float(input("Apples You Want: "))
		except ValueError:
			print("")
			print("Please input a positive number.")
			time.sleep(1)
			print("")
			continue
		if apples_to_add < 0:
			print("")
			print("Thank you for trying to give us apples. But we have a massive amount of apples, so we don't need any more.")
			time.sleep(2)
			print("")
		else:
			break
	
	global apples_remaining
	apples_remaining = apples_remaining+apples_to_add
	print("")
	print(f"{apples_to_add} Apples have been added to your apple inventory.")

# Tells the user how many apples are required to make one of each item.
def show_recipes():
	print("One Apple Pie requires 4 Apples.")
	print("One Apple Dumpling requires 3.25 Apples.")
	print("One Baked Apple requires 3 Apples.")
	print("One Apple Jam requires 2.5 Apples.")
	print("One Candy Apple required 2 Apples.")
	print("One Apple Crumble requires 1.75 Apples.")

# Shows the user how many of each thing they currently have.
def show_inventory():
	print(f"You have {apples_remaining} Apples.")
	print(f"You have {apple_pies} Apple Pies.")
	print(f"You have {apple_dumpling} Apple Dumplings.")
	print(f"You have {baked_apple} Baked Apples.")
	print(f"You have {apple_jam} Apple Jams.")
	print(f"You have {candy_apple} Candy Apples. ")
	print(f"You have {apple_crumble} Apple Crumbles. ")

# Declares global variables to be used in various functions
apples_remaining = 67
apple_pies = 0
apple_dumpling = 0
baked_apple = 0
apple_jam = 0
candy_apple = 0
apple_crumble = 0

if __name__ == "__main__":
	main()