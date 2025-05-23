#45. Jump Game II
#Solved
#Medium
#Topics
#Companies
#You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
#Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
#0 <= j <= nums[i] and
#i + j < n
#Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#
# 
#
#Example 1:
#
#Input: nums = [2,3,1,1,4]
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
#Example 2:
#
#Input: nums = [2,3,0,1,4]
#Output: 2
# 
#
#Constraints:
#
#1 <= nums.length <= 104
#0 <= nums[i] <= 1000
#It's guaranteed that you can reach nums[n - 1].
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[-1]*n
        cache[-1]=0

        for i in range(n-2,-1,-1):
            
            num=nums[i]
            if num==0:
                cache[i]=0
                continue
            minJump=sys.maxsize
            for j in range(1,num+1):
                if i+j>=n-1:
                    minJump=1
                elif cache[i+j]==0:
                    continue
                else:
                    minJump=min(minJump,1+cache[i+j])
            cache[i]=minJump

        return cache[0]




    def jumpRec(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[-1]*n
        cache[-1]=0
        

        def rec(i):
            if i>=n-1:
                return 0
            if cache[i]!=-1:
                return cache[i]
            minVal=sys.maxsize
            for j in range(1,nums[i]+1):
                minVal=min(minVal,1+rec(i+j))

            cache[i]=minVal

            return cache[i]


        rec(0)

        return cache[0]




