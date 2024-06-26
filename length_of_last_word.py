# Leetcode question:
# https://leetcode.com/problems/length-of-last-word/description/
# Description:
# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.
# A word is a maximal 
# substring
#  consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split()
        return len(word_list[-1])