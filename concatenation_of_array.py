# leetcode question: https://leetcode.com/problems/concatenation-of-array/description/

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1 = []
        num1 = nums
        nums.extend(num1)
        return nums