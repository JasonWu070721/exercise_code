# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # 搜尋範圍限制在, haystack 長度 - needle 長度
        # 從 0 開始計算到 haystack - needle 長度
        for i in range(len(haystack) - len(needle)+1):
            # 擷取 i 到 i+len(needle) 字串
            # 比對 needle 是否相同
            # 相同就回傳 haystack 在 needle 的第一個 index
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
