class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            temp = x
            rev = 0
            while x > 0:
                dig = x % 10
                rev = rev * 10 + dig
                x = x // 10
                if temp == rev:
                    return True
                else:
                    return False

