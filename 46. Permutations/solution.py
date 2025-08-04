class Solution:
    def __init__(self):
      self.permutations = []
      self.nums = []
      self.visited

    def permute(self, nums: List[int]) -> List[List[int]]:
      if len(nums) == 0:
        return []
      else:
        self.nums = nums
        self.visited = [False] * len(nums)

      def backtrack(permutation):
        # Validate solution
        if len(permutation) == len(self.nums):
          self.permutations.append(permutation) # O(1) amortized, O(n) in case of memory block resize
          return

        
        possible_nums = [num for num in self.nums if not num in permutation] # O(n) * O(k) where k is the current size of the permutation

        # Branching  
        for num in possible_nums:
          backtrack([ *permutation, num ]) # O(n!) because, it first calls for len(nums), then len(nums - 1), ... 1

      # Start backtracking  
      backtrack([])

      return self.permutations
