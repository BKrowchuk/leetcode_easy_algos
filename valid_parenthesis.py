class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2:
            return False
        dic = {'(': 1, '[': 2, '{': 3, ')': 4, ']': 5, '}': 6}
        stack = []
        valid = True
        for i in range(0, len(s)):
            curr = dic[s[i]]
            if curr < 4:
                stack.append(curr)
            else:
                if len(stack) == 0 or stack.pop() != curr-3:
                    valid = False
                    break
        if len(stack) > 0:
            return False
        return valid


a = Solution()
print(a.isValid("(()"))
