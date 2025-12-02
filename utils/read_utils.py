from typing import List

def read_input(file_path: str) -> List:
	try:
		with open(file_path, 'r') as f:
			content = f.read()
			content_split = content.split("\n")
			return content_split[:-1] # excluding the trailing empty string
	except Exception as e:
		print(f"Error {e} with reading input {file_path}")
		return []

def read_input_w_comma(file_path: str) -> List:
	try:
		with open(file_path, 'r') as f:
			content = f.read()
			content_split = content.replace("\n", "").split(",")
			return content_split
	except Exception as e:
		print(f"Error {e} with reading input {file_path}")
		return []
