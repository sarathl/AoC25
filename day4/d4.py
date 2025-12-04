from utils.read_utils import read_input
# import re
verbose = 1

def check_good_roll(roll_pos, positions, verbose):
	count = 3
	for adj_ver in range(-1, 2, 1):
		for adj_hor in range(-1, 2, 1):
			if adj_ver == 0 and adj_hor == 0:
				continue
			if roll_pos[0] + adj_ver < 0 or roll_pos[1] + adj_hor < 0:
				continue
			to_check_pos = (roll_pos[0] + adj_ver, roll_pos[1] + adj_hor)
			if to_check_pos in positions:
				count -= 1
			if count < 0:
				return False
	if verbose:
		print(f"roll pos {roll_pos} is good")
	return True

def part1():
	input_list = read_input("day4/input_example.txt")
	input_list = read_input("day4/input.txt")
	if verbose:
		print(input_list)
	positions = []
	i = 0
	for line in input_list:
		for j in range(0, len(line)):
			if line[j] == '@':
				positions.append((i,j))
		i += 1
	
	good_rolls = []
	for roll_pos in positions:
		if check_good_roll(roll_pos, positions, verbose):
			good_rolls.append(roll_pos)
	
	print(f"total rolls of paper accessible by forklift = {len(good_rolls)}")

def get_good_rolls(positions, positions_matrix):
	good_rolls = []
	for roll_pos in positions:
		if check_good_roll(roll_pos, positions, verbose):
			good_rolls.append(roll_pos)
			positions_matrix[roll_pos[0]][roll_pos[1]] = 0
	return good_rolls, positions_matrix

def part2():
	input_list = read_input("day4/input_example.txt")
	input_list = read_input("day4/input.txt")
	if verbose:
		print(input_list)
	positions = []
	positions_matrix = [[0] * len(input_list[0]) for _ in range(len(input_list))]
	i = 0
	for line in input_list:
		for j in range(0, len(line)):
			if line[j] == '@':
				positions.append((i,j))
				positions_matrix[i][j] = 1
		i += 1
	
	all_good_rolls = []
	while True:
		good_rolls, positions_matrix = get_good_rolls(positions, positions_matrix)
		positions = []
		for i in range(len(positions_matrix)):
			for j in range(len(positions_matrix[i])):
				if positions_matrix[i][j] == 1:
					positions.append((i,j))
		if len(good_rolls) == 0:
			break
		all_good_rolls.extend(good_rolls)
	print(f"total rolls of paper accessible by forklift = {len(all_good_rolls)}")

if __name__ == "__main__":
	part2()