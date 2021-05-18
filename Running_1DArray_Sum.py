class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rsum = []
        total = 0
        for i in nums:
            total += i
            rsum.append(total)
        return rsum

a  = Solution()
a.runningSum([1,2,3,4])

