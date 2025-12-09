import math
verbose = 0

def read_input(file_path: str, do_lstrip: bool = True):
	try:
		with open(file_path, 'r') as f:
			content = f.read()
			content_split = content.split("\n")
			if do_lstrip:
				return [el.lstrip() for el in content_split]
			else:
				return content_split
	except Exception as e:
		print(f"Error {e} with reading input {file_path}")
		return []

def part1():
	# input = read_input("day6/input_example.txt")
	input = read_input("day6/input.txt")
	problem_matrix = []
	for row in input:
		problem_matrix.append(row.split())
	if verbose:
		print(f"problem_matrix = {problem_matrix}")
	res = 0
	for i in range(len(problem_matrix[0])):
		nums = [int(problem_matrix[j][i]) for j in range(len(problem_matrix)-1)]
		if problem_matrix[-1][i] == "*":
			res += math.prod(nums)
		else:
			res += sum(nums)
	print(f"total of answers = {res}")

def part2():
	# input = read_input("day6/input_example.txt", do_lstrip=False)
	input = read_input("day6/input.txt", do_lstrip=False)
	if verbose:
		print(f"input = {input}")
	reset_number_list = False
	res = 0
	number_list = []
	for i in range(len(input[0])-1, -1, -1):
		number_str = ""
		for j in range(len(input)):
			try:
				num = int(input[j][i])
				number_str += str(num)
			except:
				if input[j][i] == '*':
					number_list.append(int(number_str))
					value = math.prod(number_list)
					res += value
					if verbose:
						print(f"number_list = {number_list}")
						print(f"value = {value}")
					number_list = []
					number_str = ''
					continue
				elif input[j][i] == '+':
					number_list.append(int(number_str))
					value = sum(number_list)
					res += value
					if verbose:
						print(f"number_list = {number_list}")
						print(f"value = {value}")
					number_list = []
					number_str = ''
					continue
				continue
		try:
			number_list.append(int(number_str))
		except:
			continue
		if verbose:
			print(f"number_list = {number_list}")
	print(f"total of answers = {res}")

if __name__ == "__main__":
	part2()