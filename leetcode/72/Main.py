# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # 很難, 研究中
        # word1 經過以下動作, 如何變成 word2,
        # 做最少次數
        # Insert a character
        # Delete a character
        # Replace a character
        # 標準的動態規劃
        # 只考慮最後一個字
        #

        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j],
                                          table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]

        # TLE
        """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)
