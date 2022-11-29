# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 2維陣列指標移動
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        print(up, down, left, right)
        ans = []
        while True:
            # 向右加
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            if up > down:
                break
             # 向下加
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            # 向左加
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if down < up:
                break
             # 向上加
            for i in range(down, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans
