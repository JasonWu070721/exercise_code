# 263. Ugly Number
class Solution:
    def isUgly(self, num: int) -> bool:
        # 那麼最直接的辦法就是不停的除以這些質數，如果剩餘的數字是1的話就是醜陋數了：
        if num < 1:
            return False
        while num > 0:
            if num == 1:
                return True
            # 如果可以被2除, 就除以2
            elif num % 2 == 0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
            else:
                return False
