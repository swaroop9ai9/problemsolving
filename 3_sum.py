#from itertools import combinations()
''' Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which gives
the sum of zero.

Note:

The solution set must not contain duplicate triplets.'''
import datetime
from itertools import combinations
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = set()
        bgtime = datetime.datetime.now()
        for i in list(combinations(nums,3)):
            if sum(i)==0:
                d.add(tuple(sorted(i)))
        #out = list(set(tuple(sorted(sub)) for sub in d))
        r = [d,bgtime]
        return r

sol1 = Solution()
d = sol1.threeSum(list(map(int,input().split(','))))
print(d[0])
print(datetime.datetime.now() - d[1])

# Other's Solution
class Solu:
    def threeSum(self, nums):
        bgtime = datetime.datetime.now()
        res = []
        zero_count = nums.count(0)
        if zero_count >= 3:
            res.append([0, 0, 0])
            [nums.remove(0) for _ in range(0, zero_count - 1)]
        
        nums = sorted(nums)
        pGroup, nGroup = [], []
        for n in nums:
            if n >= 0:
                pGroup.append(n)
            else:
                nGroup.append(n)
        nlen, plen = len(nGroup), len(pGroup)
        pSet, nSet = set(pGroup), set(nGroup)
        
        if len(nGroup) >= 2:
            previous_a = None
            for i in range(nlen - 1):
                a = nGroup[i]
                previous_b = None
                if previous_a == a:
                    continue

                for j in range(i + 1, nlen):
                    b = nGroup[j]
                    if previous_b == b:
                        continue
                    
                    if -(a + b) in pSet:
                        res.append([-(a + b), a, b])
                    previous_b = b
                previous_a = a
                
        if len(pGroup) >= 2:
            previous_a = None
            for i in range(plen - 1):
                a = pGroup[i]
                previous_b = None
                if previous_a == a:
                    continue

                for j in range(i + 1, plen):
                    b = pGroup[j]
                    if previous_b == b:
                        continue
                        
                    if -(a + b) in nSet:
                        res.append([-(a + b), a, b])
                    previous_b = b
                previous_a = a
        r = [res,bgtime]
        return r
s2 = Solu()   
dr = s2.threeSum(list(map(int,input().split(','))))
print(dr[0])
print(datetime.datetime.now() - dr[1])


