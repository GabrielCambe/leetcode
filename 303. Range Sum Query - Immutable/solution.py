class NumArray:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.prefixArray = []
        
        acc = 0
        for num in self.array:
            acc += num
            self.prefixArray.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixArray[right] - self.prefixArray[left] + self.array[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)