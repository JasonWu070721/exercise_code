# 216. Combination Sum III
# backtracking
# 找出所有相加上和為 n 的 k 個數的組合。組合中只允許含有 1 - 9 的正整數，並且每種組合中不存在重複的數字。
# 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
class Solution:

    # backtracking solution
    # 與題目 77 相同, 只是過濾要儲存合等於 k的集合
    def __init__(self):
        self.res = []
        self.sum_now = 0
        self.path = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1)
        return self.res

    def backtracking(self, k: int, n: int, start_num: int):
        if self.sum_now > n:  # 剪枝
            return
        if len(self.path) == k:  # len(path)==k時不管sum是否等於n都會返回
            if self.sum_now == n:
                self.res.append(self.path[:])
            return
        for i in range(start_num, 10 - (k - len(self.path)) + 1):
            self.path.append(i)
            self.sum_now += i
            self.backtracking(k, n, i + 1)
            self.path.pop()
            self.sum_now -= i
