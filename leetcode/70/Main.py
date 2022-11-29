# 70. Climbing Stairs
# 空間複雜度為O(n)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 為第 i 階樓梯有多少種方法爬到樓頂
        dp = [0]*(n+1)
        dp[1] = 1

        # 當 n 為 1, dp[2] 會 over point
        if n is 1:
            return 1

        dp[2] = 2
        for i in range(3, n+1):
            # dp[i - 1]，上i-1層樓梯，有dp[i - 1]種方法，那麼再一步跳一個台階就是dp[i]
            # dp[i - 2]，上i-2層樓梯，有dp[i - 2]種方法，那麼再一步跳兩個台階就是dp[i]了
            # dp[i]就是 dp[i - 1]與dp[i - 2]之和
            # 這是 Fibonacci sequence
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

# 空間複雜度為O(1)版本


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            tmp = dp[0]+dp[1]
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[1]
