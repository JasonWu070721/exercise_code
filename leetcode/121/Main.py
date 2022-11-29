class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])  # 取最左最小價格
            result = max(result, prices[i] - low)  # 直接取最大區間利潤
        return result

# 動態規劃：版本一


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if len == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[-1][1]


# 動態規劃：版本二
# 還無法理解

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0] * 2 for _ in range(2)]  # 注意這裡只開闢了一個2 * 2大小的二維陣列

        # dp[i][0] 表示第i天持有股票所得最多現金
        # dp[i][1] 表示第i天不持有股票所得最多現金

        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i % 2][0] = max(dp[(i-1) % 2][0], -prices[i])
            dp[i % 2][1] = max(dp[(i-1) % 2][1], prices[i] + dp[(i-1) % 2][0])
        return dp[(length-1) % 2][1]

# 動態規劃：版本三


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp0, dp1 = -prices[0], 0  # 注意這裡只維護兩個常數，因為dp0的更新不受dp1的影響
        for i in range(1, length):
            dp1 = max(dp1, dp0 + prices[i])
            dp0 = max(dp0, -prices[i])
        return dp1
