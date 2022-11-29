# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # print(len(s))
        # print(numRows)
        # 考邏輯, array 應用
        # 先略過
        if numRows == 1 or numRows >= len(s):
            return s
        # 建立 numRows 空字串陣列, 長度為 numRows
        L = [''] * numRows
        index, step = 0, 1
        # s 為輸入所有字串
        # index 為要插入 L 中 array 的哪一個 index
        # step 是計算要插入哪一個 index
        # step 邏輯是 [159, 2468, 37], 像是在 array 內打回彈球, 左右擺動
        for x in s:
            # print("index:", index)
            L[index] += x
            # print("L:", L)
            # 當道了 array 的第一個, step 改用+的
            if index == 0:
                step = 1
            # 當道了 array 的最後一個, step 改用-的
            elif index == numRows -1:
                step = -1
            index += step
            
            # print("step:", step)
            # print("----")

        return ''.join(L)