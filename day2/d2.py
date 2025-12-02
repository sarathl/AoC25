from utils.read_utils import read_input_w_comma
import re
VERBOSE = 0

def get_nums(input):
	num1, num2 = input.split("-")[0], input.split("-")[1]
	return num1, num2

def check_num_bw_range(num_to_check, num1, num2):
	if int(num_to_check) >= int(num1) and int(num_to_check) <= int(num2):
		return True
	return False

def part1():
	# input_list = read_input_w_comma("day2/input_example.txt")
	input_list = read_input_w_comma("day2/input.txt")
	if VERBOSE:
		print(input_list)
	res = []
	for el in input_list:
		num1, num2 = get_nums(el)
		if VERBOSE:
			print(num1, num2)
		try:
			left_half_num = int(num1[:len(num1)//2])
		except:
			left_half_num = 0
		try:
			if len(num2) % 2 == 0:
				right_half_num = int(num2[:len(num2)//2])
			else:
				right_half_num = int(num2[:len(num2)//2 + 1]) # taking floor in case it's odd digited number as max range
		except:
			right_half_num = 0
		if VERBOSE:
			print(left_half_num, right_half_num)
		while left_half_num <= right_half_num:
			full_num = str(left_half_num) + str(left_half_num)
			if check_num_bw_range(full_num, num1, num2):
				res.append(int(full_num))
				if VERBOSE:
					print(f"full num is {full_num}")
			left_half_num += 1
	# if VERBOSE:
	# 	print(res)
	print(f"part 1 answer is {sum(res)}")

def part2():
	# input_list = read_input_w_comma("day2/input_example.txt")
	input_list = read_input_w_comma("day2/input.txt")
	if VERBOSE:
		print(input_list)
	res = []
	for input in input_list:
		num1, num2 = get_nums(input)
		if VERBOSE:
			print(num1, num2)
		for el in range(int(num1), int(num2)):
			re_pattern = re.compile(r"^(.+)\1+$")
			if re_pattern.match(str(el)):
				res.append(el)
	if VERBOSE:
		print(res)
	print(f"part 2 answer is {sum(res)}")

if __name__ == "__main__":
	part2()
