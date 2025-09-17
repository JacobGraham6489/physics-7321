# test file

list1 = [1, 2, 3, 4, 5]

def append_five(target_list):
	"""Append the integer 5 to target_list in-place and return it.

	Args:
		target_list (list): list to append to

	Returns:
		list: the same list after appending 5
	"""
	target_list.append(5)
	return target_list

if __name__ == "__main__":
	print("original:", list1)
	append_five(list1)
	print("after append_five:", list1)

# end
print("Hello World!")
x = 42
type(x)
print(type(x))
list1 = [1, 2, 3, 4, 5]
list1[4] = 3
print(list1)

