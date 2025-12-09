verbose = 0

def read_input(file_path: str):
	try:
		with open(file_path, 'r') as f:
			content = f.read()
			content_split = content.split("\n")
			fresh_list = []
			available_ingredients = []
			# if verbose:
			# 	print(content_split)
			# 	print("splitting the content")
			for i in range(len(content_split)):
				if content_split[i] == "":
					break
				fresh_list.append([int(content_split[i].split('-')[0]), int(content_split[i].split('-')[1])])
			available_ingredients.extend(content_split[i+1:])
			if verbose:
				print(fresh_list)
				print(available_ingredients)
			return fresh_list, available_ingredients
	except Exception as e:
		print(f"Error {e} with reading input {file_path}")
		return []

def check_if_ing_is_fresh(fresh_list, ing_id):
	for range in fresh_list:
		if range[0] <= ing_id <= range[1]:
			return True
	return False
	# fresh_list is sorted
	# l = 0
	# r = len(fresh_list) - 1
	# while l <= r:
	# 	mid = (l + r) // 2
	# 	if fresh_list[mid] == ing_id:
	# 		return True
	# 	elif fresh_list[mid] < ing_id:
	# 		l = mid + 1
	# 	else:
	# 		r = mid - 1
	# return False

def part1():
	# fresh_list, available_ingredients = read_input("day5/input_example.txt")
	fresh_list, available_ingredients = read_input("day5/input.txt")
	fresh_and_available_ingredients = []
	if verbose:
		print(fresh_list)
		print(available_ingredients)
	for ing_id in available_ingredients:
		if check_if_ing_is_fresh(fresh_list, int(ing_id)):
			if verbose:
				print(f"{ing_id} is fresh")
			fresh_and_available_ingredients.append(ing_id)
		else:
			if verbose:
				print(f"{ing_id} is not fresh")
	
	print(f"total fresh and available ingredients = {len(fresh_and_available_ingredients)}")

def part2():
	# fresh_list, available_ingredients = read_input("day5/input_example.txt")
	fresh_list, available_ingredients = read_input("day5/input.txt")
	fresh_ingredients = []
	if verbose:
		print(fresh_list)
	fresh_list_sorted = sorted(fresh_list)
	if verbose:
		print(f"sorted fresh list is {fresh_list_sorted}")
	unique_ranges = [fresh_list_sorted[0]]
	for i in range(1, len(fresh_list_sorted)):
		prev_range = unique_ranges[-1]
		curr_range = fresh_list_sorted[i]
		if curr_range[0] > prev_range[1]:
			unique_ranges.append(curr_range)
		else:
			unique_ranges[-1][1] = max(prev_range[1], curr_range[1])
	if verbose:
		print(f"unique ranges are {unique_ranges}")
	distinct_fresh_count = 0
	for range_list in unique_ranges:
		distinct_fresh_count += range_list[1] - range_list[0] + 1
	print(f"total fresh ingredients = {distinct_fresh_count}")

if __name__ == "__main__":
	part2()