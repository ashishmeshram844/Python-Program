"""
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t = 0
        n = []
        for i in range(len(nums)):
            t = t+nums[i]
            n.append(t)
        return n


