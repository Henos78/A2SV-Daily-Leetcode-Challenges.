class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Using extra space
        num = [i for i in range(0, len(nums)+1)]
        
        for i in num:
            if i not in nums:
                return i
        