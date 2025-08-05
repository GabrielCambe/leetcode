class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    power_set = []
        
    def backtrack(start_index: int, current_subset: List[int]):
      # Validation:
      # No specific validation is needed since the branching
      # is implemented such that no previously chosen element
      # will be added again, so we can just
      # add the current subset to the power set
      power_set.append(list(current_subset))
            
      # Branching:
      # We now choose all elements from start_index to len(nums)-1
      for i in range(start_index, len(nums)):
        # generate a new subset
        current_subset.append(nums[i])                

        # recursively call backtrack, but now we do not choose element i
        # since it is already in the current subset,
        # and we will generate new ones form it
        backtrack(i + 1, current_subset)
        
        # Backtrack:
        # We remove the previously added element so we can
        # explore new solutions
        current_subset.pop()

    # Start by choosing elements 0,1,2,..,len(nums)-1
    # and with the current subset being the empty subset
    backtrack(0, [])
        
    return power_set
