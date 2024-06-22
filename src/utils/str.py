def _get_size_diffs(categories: list[list[str]]) -> list[int]:
	max_length = []
	for row in categories:
		for i, elem in enumerate(row):
			if i >= len(max_length):
				max_length.append(len(elem))
			elif len(elem) > max_length[i]:
				max_length[i] = len(elem)
	return max_length

def get_aligned_text(categories: list[list[str]], sep: str, nb: int) -> str:
	max_length = _get_size_diffs(categories)
	result = ""
	for row in categories:
		for i, elem in enumerate(row):
			result += elem
			if i != len(row)-1:
				result += sep * (max_length[i]-len(elem)+nb)
			else:
				result += "\n"
	print(result)
	return result
