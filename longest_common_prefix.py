class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        for i in strs:
            if len(i) == 0:
                return ""
        same_char = True
        prefix_size = 0
        while same_char:
            for i in strs:
                if len(i) <= prefix_size or i[prefix_size] != strs[0][prefix_size]:
                    same_char = False
                    break
            prefix_size += 1
        return strs[0][0:prefix_size-1]


a = Solution()
b = a.longestCommonPrefix(["flower", "flow", "flight"])
print(b)
