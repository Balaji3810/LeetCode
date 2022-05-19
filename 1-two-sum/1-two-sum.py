class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       # l, r = 0, len(nums)-1
       # 
       # while l < r:
       #     twoSum = nums[l] + nums[r]
       #     
       #     if twoSum == target:
       #         return l, r
       #         break
       #     elif twoSum < target:
       #         l += 1
       #     else:
       #         r -= 1
       # 
        
        #for i in range(len(nums)):
        #    for j in range(len(nums)):
        #        if i != j:
        #            twoSum = nums[i] + nums[j]
        #            if twoSum == target:
        #                return i, j
        #                break
         
        prevMap = {} #val : index
        
        for i, n in enumerate(nums):
            
            diff = target - n
            
            if diff in prevMap:
                return [prevMap[diff],i]
            
            else:
                prevMap[n] = i
        return
        