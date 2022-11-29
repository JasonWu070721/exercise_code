# 322. Coin Change
# 給定不同面額的硬幣 coins 和一個總金額 amount。編寫一個函數來計算可以湊成總金額所需的最少的硬幣個數。
# 如果沒有任何一種硬幣組合能組成總金額，返回 -1。
# Dynamic Programming
# 1. dp[j]：湊足總額為j所需錢幣的最少個數為dp[j]
# 2. 遞推公式：dp[j] = min(dp[j - coins[i]] + 1, dp[j]);
# 如果求組合數就是外層for循環遍歷物品，內層for遍歷背包。
# 如果求排列數就是外層for遍歷背包，內層for循環遍歷物品。
# 研究中...
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''版本一'''
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        '''版本二'''
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for j in range(1, amount + 1):
            # 遍历背包
            for coin in coins:
                if j >= coin:
                    dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
