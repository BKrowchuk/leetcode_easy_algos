class Solution(object):
    def romanToInt(self, s):   
        dic = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev = 0
        curr = 0 
        total = 0
        for i in range(0, len(s)):
            curr = dic[s[i]]
            total += curr
            if prev < curr and prev > 0: 
                total -= 2*prev
            prev = curr
        return total

a = Solution()
print(a.romanToInt("III"))
