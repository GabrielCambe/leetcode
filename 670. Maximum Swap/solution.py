class Solution:
	def maximumSwap(self, num: int) -> int:
		# Get all digits (O(n) time and O(n) space, where n is the number of digits in the number)
		digits = [num % 10]
		j = num // 10
		while (j > 0):
			digits.append(j % 10)
			j = j // 10
		digits.reverse()
		n = len(digits)

		# Use a dictionary to store the last seen index of each digit.
		# This allows for O(1) lookup of a digit's rightmost position.
		last_occurrence = {digit: i for i, digit in enumerate(digits)}

		# Iterate through the digits from left to right (most significant to least).
		for i in range(n):
			current_digit = digits[i]
			
			# Search for a larger digit in the dictionary (from 9 down to current_digit + 1).
			for d in range(9, current_digit, -1):
				
				# Check if a larger digit exists
				if d in last_occurrence:
					
					# Get the index of the rightmost occurrence of this larger digit.
					swap_idx = last_occurrence[d]
					
					# If the larger digit is to the right of the current digit,
					# we've found the optimal swap.
					if swap_idx > i:
						
						# Perform the swap.
						digits[i], digits[swap_idx] = digits[swap_idx], digits[i]
						
						# Since we can only swap once, return the new number immediately.
						# We calculate the number from its digits and return						
						new_number = 0
						factor = len(digits)-1
						for k in digits:
							new_number += k * (10 ** factor)
							factor -= 1
						return new_number

		# If the loop completes, no swap was needed. The number is already the maximum.
		return num