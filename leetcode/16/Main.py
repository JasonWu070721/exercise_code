# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l, r = i + 1, n - 1
            # l 左指標, r 右指標, 當l, r 相交就停止.
            while l < r:
                # ans 上一個和, sum3 目前的和
                sum3 = nums[i] + nums[l] + nums[r]
                # 比較最小的, 如果 sum3 更小, ans 就被複寫
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target:
                    return target
                if sum3 > target:
                    r -= 1  # Sum3 is greater than the target, to minimize the difference, we have to decrease our sum3
                else:
                    l += 1  # Sum3 is lesser than the target, to minimize the difference, we have to increase our sum3
        return ans
