from utils.read_utils import read_input
# import re
verbose = 0

def part1():
	# input_list = read_input("day3/input_example.txt")
	input_list = read_input("day3/input.txt")
	if verbose:
		print(input_list)
	max_list = []
	for bank in input_list:
		current_max = 0
		max_starting_digit = 0
		bank_str = str(bank)
		for i in range(len(bank_str)-1):
			if int(bank_str[i]) < max_starting_digit:
				continue
			max_starting_digit = max(max_starting_digit, int(bank_str[i]))
			max_2_digit_possible = bank_str[i] + max(bank_str[i+1:])
			current_max = max(current_max, int(max_2_digit_possible))
		max_list.append(current_max)	
	if verbose:
		print(f"List of max possible joltages: {max_list}")
	print(f"Total output joltage: {sum(max_list)}")

def part2():
	input_list = read_input("day3/input_example.txt")
	input_list = read_input("day3/input.txt")
	if verbose:
		print(input_list)
	max_list = []
	for bank in input_list:
		bank_str = str(bank)
		joltage = ""
		next_pos, curr_pos = 0, 0
		for i in range(1,13):
			max_int = 0
			for j in range(next_pos, len(bank_str) - (12-i)):
				if int(bank_str[j]) > max_int:
					max_int = int(bank_str[j])
					curr_pos = j
			next_pos = curr_pos + 1
			joltage += str(max_int)
		max_list.append(int(joltage))

	if verbose:
		print(f"List of max possible joltages: {max_list}")
	print(f"Total output joltage: {sum(max_list)}")

if __name__ == "__main__":
	part2()