# Math question
# sum(original) + m * (n - 1) = sum(final), where m is the number of adds
# sum(final) = x * n, where x is the final number
# x = min(original) + m

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)