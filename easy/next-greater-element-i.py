class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        idx_dict = dict()
        larger_nums = []
        
        # Use dictionary to cache idx ordering
        for idx, num in enumerate(nums):
            idx_dict[num] = idx
        
        # Iterate through and check for larger number
        for num in findNums:
            found = False
            num_idx = idx_dict[num]
            while num_idx < nums_len - 1:
                num_idx += 1
                
                if nums[num_idx] > num:
                    larger_nums.append(nums[num_idx])
                    found = True
                    break
                    
            if not found:
                larger_nums.append(-1)
                
        return larger_nums