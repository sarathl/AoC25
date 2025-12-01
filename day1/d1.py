from utils.read_utils import read_input
VERBOSE = 0

def part1():
	input_list = read_input("day1/input.txt")
	running_sum, prev_running_sum = 50, 50
	result1, result2 = 0, 0
	running_sum_rest = False
	for el in input_list:
		current_steps = int(el[1:])
		if el[0] == 'L':
			running_sum -= current_steps
		else:
			running_sum += current_steps
		if running_sum%100 == 0:
			result1 += 1
		running_sum = running_sum % 100 # to convert everything to positive
		remainder = current_steps % 100
		if prev_running_sum > 0:
			if el[0] == 'L':
				if remainder > prev_running_sum:
					result2 += 1
			else:
				if remainder + prev_running_sum > 100:
					result2 += 1
		result2 += current_steps//100

		prev_running_sum = running_sum
		if VERBOSE:
			print(f"el is {el}")
			print(f"run sum is {running_sum}")
			print(f"prev run sum is {prev_running_sum}")
			print(f"result2 is {result2}")
	result2 += result1
	print(f"part 1 answer is {result1}")
	print(f"part 2 answer is {result2}")

if __name__ == "__main__":
	part1()
