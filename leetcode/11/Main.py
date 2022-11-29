# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        # r 從最右邊, l 從最左邊往中間移動
        # area 要找最大面積
        while l < r:
            # 計算最大的面積
            # (r - l) * min(height[l], height[r])
            # 
            area = max(area, (r - l) * min(height[l], height[r]))
            # 要找左邊最高和右邊最高的 l 和 r
            # 如果右邊 r 比較高, l 就像右移動
            # 如果左邊 l 比較高, r 就像左邊移動
            # print(height[l])
            # print(height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return area