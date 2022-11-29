# 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # print(list(mapping[digits[0]]))
        if len(digits) == 0:
            return []
        # 剩下一個數字, 組合就是那個數字的所有字串
        if len(digits) == 1:
            # list 會將字串拆字, 轉成 array
            return list(mapping[digits[0]])

        # 遞迴解法
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]
