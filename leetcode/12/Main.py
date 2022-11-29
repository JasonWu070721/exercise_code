# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        # Init
        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        # 遇到4、9開頭的數字另外處理
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        
        # Loop
        for i in range(len(nums)):
            # 只有大於 nums 內數字才要計算
            if (num >= nums[i]):
                print(i)
                print(symbol[i])
               
                print(num)
                print(nums[i])
                # (num // nums[i]) num 是要處理剩下的 Roman, nums[i] 是 nums 裡可用的最小數字
                # symbol[i] 是可用的最小 Roman
                # * 是要多少的最小 Roman
                result += symbol[i] * (num // nums[i])
                print(result)
                num %= nums[i]
        
        return result;