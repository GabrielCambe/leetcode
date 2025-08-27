class Solution:
	def minimumDeletions(self, nums: List[int]) -> int:	
		# Find min and max
		min_idx = 0
		max_idx = 0
		for i in range(1,len(nums)):
			if (nums[i] > nums[max_idx]):
				previous_max_idx = max_idx
				max_idx = i
				if nums[previous_max_idx] < nums[min_idx]:
					min_idx = previous_max_idx
			elif (nums[i] < nums[min_idx]):
				min_idx = i
		
		# print(f"min_idx: {min_idx}, max_idx: {max_idx}")

		# Find number of deletions
		deleting_from_beggining = (min_idx if min_idx > max_idx else max_idx) + 1
		deleting_from_end = len(nums) - (min_idx if min_idx < max_idx else max_idx)
		from_both_ends = len(nums) - (min_idx if min_idx > max_idx else max_idx) + (min_idx if min_idx < max_idx else max_idx) + 1
		
		# print(f"deleting_from_beggining: {deleting_from_beggining}, deleting_from_end: {deleting_from_end}, from_both_ends: {from_both_ends}")

		min_deletions = min(deleting_from_beggining, deleting_from_end, from_both_ends)
		return min_deletions
