'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
 Hint #1  
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. 
If we fix one of the numbers say x, we are left with the two-sum problem at hand!
 Hint #2  
For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y
which is value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?
 Hint #3  
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

'''
#Solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while(l<r):
                sum = nums[i] + nums[l] + nums[r]
                if sum<0:
                    l+=1
                elif sum >0:
                    r-=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l<len(nums)-1 and nums[l] == nums[l + 1] : l += 1
                    while r>0 and nums[r] == nums[r - 1]: r -= 1
                    l+=1
                    r-=1
        return result
        
        
        
        
