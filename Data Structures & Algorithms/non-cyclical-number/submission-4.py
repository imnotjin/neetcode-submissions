class Solution:
    def isHappy(self, n: int) -> bool:
        def check(num):
            res = 0
            while num:
                res += (num % 10) ** 2
                num //= 10
            return res
        
        slow = fast = n
        while fast:
            slow = check(slow)
            fast = check(check(fast))
            if slow == 1:
                return True
            if slow == fast:
                return False
        return False
