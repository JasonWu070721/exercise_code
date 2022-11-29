# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        # print("left:",left)
        # print("right:",right)
        # print("string:",string)
        # print("ans:",ans)
        # print("----")
        # right 是 right 括號剩下多少個可以用
        # left 是 left 括號剩下多少個可以用
        # right 可用括號數量不能小於 left 可用括號數量, 因左邊目前的括號數量必>=於右邊的目前的括號數量
        if right < left:
            return
        # 當左右括號都用完了, 就將 string append to ans, 然後 return
        if not left and not right:
            ans.append(string)
            return
        # 這遞迴可表顯出一個 Tree
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")
