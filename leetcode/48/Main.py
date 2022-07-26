# 48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        # 水平翻轉
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i -
                                     1][j] = matrix[n - i - 1][j], matrix[i][j]

        print(matrix)

        # 主對角線翻轉
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
