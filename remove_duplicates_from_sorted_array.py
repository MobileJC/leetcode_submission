# leetcode question link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        for check_index in range(1, len(nums)):
            if nums[check_index] != nums[check_index - 1]:
                nums[index] = nums[check_index]
                index += 1
        return index