class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # returns the indices of the 2 numbers that add to the target (exactly one solution)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

a = Solution()
print(a.twoSum([2,7,20], 27)) 
