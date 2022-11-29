# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        # str(abs(x))[::-1], 反轉字串
        # 再轉成 int
        rev = int(str(abs(x))[::-1])

        # 如果超過 32 bit, return 0
        if rev.bit_length() < 32:
            # 判斷是否為負數, 如果x小於0, 加上負數
            return (-rev if x < 0 else rev)
        else:
            return 0