"""
File: largest_digit.py
Name: Alan Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	adjust the input number into positive integer and get the units digit of the input number.
	:param n: (int) the input integer
	"""
	if n < 0:
		n = -n
	l = n % 10
	return find_largest_digit_helper(n, l)


def find_largest_digit_helper(n, l):
	"""
	helper function
	base case: n//10 == 0
	n//10 => remove the units digit of n
	n%10 => get the units digit of n
	:param n: (int) the number which units digit are removing.
	:param l: (int) the stored largest digit so far
	"""
	if n//10 == 0:  # base case: no more digits after removal of units digit
		if n % 10 > l:  # if this number is larger than the largest digit so far.
			l = n % 10
		return l
	else:  # recursive case: still have more than 1 digit.
		if n % 10 > l:  # if this number is larger than the largest digit so far.
			l = n % 10
		return find_largest_digit_helper(n//10, l)


if __name__ == '__main__':
	main()
