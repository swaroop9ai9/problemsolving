# Array 1 - Two Sum
'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.'''
'''

Example
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. '''

''' MY SOLUTION
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target/2 == nums[i]:
                continue
            elif target-nums[i] in nums:
                a = i
                b = nums.index(target-nums[i])
                return [a,b]
sol1 = Solution()
print(sol1.twoSum(list(map(int,input().split())),int(input())))'''

class Solution:
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [i, d[target-nums[i]]] 
            
            if nums[i] not in d:
                d[nums[i]] = i
sol2 = Solution()
print(sol2.twoSum(list(map(int,input().split())),int(input())))



        
