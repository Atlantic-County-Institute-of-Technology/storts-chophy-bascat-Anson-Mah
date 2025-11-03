# Name: Anson Mah
# Date: October 2025

import random
import os
import time

def main():
	while True:
		# Initial Menu
		print("")
		print("[0]. Quit Program")
		print("[1]. View Current List")
		print("[2]. Generate New List")
		print("[3]. Sort List")
		print("[4]. View Sorting Statistics")
		# print("[5]. Developer's List")

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
				view_list()
			case 2:
				generate_new_list()
			case 3:
				sort_list()
			case 4:
				view_sorting_statistics()

			# Code for Development Purposes. It creates a list without having to manually input the arguments.
			# case 5:
			# 	global numbers
			# 	numbers = [random.randint(-1000,1000) for i in range(1500)]
			# 	print("")
			# 	print(numbers)

def generate_new_list():
	global numbers
	global lists_generated

	# Input Validation
	# Only allows integers
	while True:
		try:
			lower_bound = int(input("Input the Lower Bound: "))
			break
		except ValueError:
			print("Please input a valid integer.")

	# Input Validation
	# Only allows integers greater than the Lower Bound
	while True:
		try:
			upper_bound = int(input("Input the Upper Bound: "))
		except ValueError:
			print("Please input a valid integer.")
			continue
		if upper_bound < lower_bound:
			print("Your Upper Bound must be greater than your Lower Bound.")
		else:
			break

	# Input Validation
	# Only allows positive integers
	while True:
		try:
			amount_of_numbers = int(input("Input the amount of numbers in the list: "))
		except ValueError:
			print("Please input a valid integer.")
			continue
		if amount_of_numbers <= 0:
			print("You must input a positive integer.")
		else:
			break
	
	numbers = [random.randint(lower_bound,upper_bound) for i in range(amount_of_numbers)]
	lists_generated = lists_generated + 1
	print("")
	print("A new list has been generated.")

def view_list():
	global numbers
	if numbers == []:
		print("You have not generated a list yet.")
	else:
		print(numbers)
		print(f"Sorted: {str(check_if_sorted(numbers))}")

def sort_list():
	global numbers
	global lists_sorted
	global bubble_sorts_used
	global insertion_sorts_used
	global selection_sorts_used

	if numbers == []:
		print("You do not have a list.")
		return
	elif check_if_sorted(numbers) == True:
		print("Your list is already sorted.")
		return

	print("[1]. Bubble Sort")
	print("[2]. Insertion Sort")
	print("[3]. Selection Sort")

	# Input Correction
	# If the user's input would break the program, it changes the input such that it will not break the program.
	while True:
		try:
			desired_sorting_algorithm = int(input("Select your desired Sorting Algorithm: "))
			break
		except ValueError:
			# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the food menu
			desired_sorting_algorithm = 9
			break

	print("")
	timer_start = time.perf_counter()  # Starts a timer. In future lines of code, the timer is stopped. This is to recored the amount of time it takes for the sorting algorithm to sort the list.
	
	match desired_sorting_algorithm:
		case 1:
			bubble_sorts_used = bubble_sorts_used + 1
		case 2:
			insertion_sorts_used = insertion_sorts_used + 1
		case 3:
			selection_sorts_used = selection_sorts_used + 1

	# Stops the timer that was started earlier. This recoreds the amount of time it takes for the sorting algorithm to sort the list.
	timer_end = time.perf_counter()
	time_elapsed = timer_end - timer_start
	print(f"Runtime: {time_elapsed} seconds")

	lists_sorted = lists_sorted + 1

def view_sorting_statistics():
	global lists_generated
	global lists_sorted
	global bubble_sorts_used
	global insertion_sorts_used
	global selection_sorts_used

	print(f"Lists Generated: {lists_generated}")
	print(f"Total Lists Sorted: {lists_sorted}")
	print(f"Lists Sorted using Bubble Sort: {bubble_sorts_used}")
	print(f"Lists Sorted using Insertion Sort: {insertion_sorts_used}")
	print(f"Lists Sorted using Selection Sort: {selection_sorts_used}")

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

# Checks to see if the list is sorted or not
def check_if_sorted(list):
	for i in range(len(list)-1):
		j = i + 1
		if list[i] > list[j]:
			return False
	return True

# Creates empty list
numbers = []

# Sorting Statistics
lists_generated = 0
lists_sorted = 0
bubble_sorts_used = 0
insertion_sorts_used = 0
selection_sorts_used = 0

if __name__ == "__main__":
	main()