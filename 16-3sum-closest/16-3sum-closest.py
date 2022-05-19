class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        
        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            
            if i > 0 and nums[i-1] == a:
                continue
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if abs(threeSum - target) < abs(res - target):
                    res = threeSum
                
                if threeSum > target:
                    r -= 1
                else:
                    l += 1
        return res
        