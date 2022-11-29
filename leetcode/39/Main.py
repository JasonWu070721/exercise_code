# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        self.dfs(candidates, target, [], ret)
        return ret

    # dfs 一個 tree
    # tree: https://zxi.mytechroad.com/blog/searching/leetcode-39-combination-sum/
    # tree 的每n層, 表示每n-1個輸入的組合
    # target 因已經計算過的殘值, 再用殘值繼續減, 直到0, 表示 ret 加起來為0
    def dfs(self, nums, target, path, ret):
        # print(nums)
        # print(target)
        # print(path)
        # print("----")

        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
