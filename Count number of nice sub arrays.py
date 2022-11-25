class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, 0 #Lets assume we have two pointers
        oddCount = 0
        res = 0
        subArray_count = 0

        for p1 in range(len(nums)):
            if nums[p1] %2 == 1:
                oddCount += 1
                subArray_count = 0

            while oddCount == k:
                if nums[p2] %2 ==1:
                    oddCount -= 1
                subArray_count += 1
                p2 += 1

            res += subArray_count

        return res