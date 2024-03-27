from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0;
        right=1;
        maxSum=nums[0]
        sum=nums[0]
        while right<len(nums):
            if nums[left]<=0:
                sum-=nums[left]
                left+=1
                maxSum=max(sum,maxSum)
            if nums[right]>0:
                sum+=nums[right]
                right+=1
                maxSum=max(sum,maxSum)
        
