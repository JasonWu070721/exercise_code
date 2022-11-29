# 40. Combination Sum II
class Solution:

    def __init__(self):
        self.paths = []
        self.path = []
        self.used = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        類似於求三數之和，求四數之和，為了避免重複組合，需要提前進行陣列排序
        本題需要使用used，用來標記區別同一樹層的元素使用重複情況：注意區分遞迴縱向遍歷遇到的重複元素，和for循環遇到的重複元素，這兩者的區別
        '''
        self.paths.clear()
        self.path.clear()
        self.usage_list = [False] * len(candidates)
        # 必須提前進行陣列排序，避免重複
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return

        # 單層遞迴邏輯
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.組合總和
            if sum_ + candidates[i] > target:
                return

            # 檢查同一樹層是否出現曾經使用過的相同元素
            # 若陣列中前後元素值相同，但前者卻未被使用(used == False)，說明是for loop中的同一樹層的相同元素情況
            if i > 0 and candidates[i] == candidates[i-1] and self.usage_list[i-1] == False:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.usage_list[i] = True
            self.backtracking(candidates, target, sum_, i+1)
            self.usage_list[i] = False  # 回溯，為了下一輪for loop
            self.path.pop()             # 回溯，為了下一輪for loop
            sum_ -= candidates[i]       # 回溯，為了下一輪for loop
