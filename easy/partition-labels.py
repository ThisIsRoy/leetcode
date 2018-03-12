class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        str_lens = []
        last = dict()
        
        for char_idx in range(len(S)):
            last[S[char_idx]] = char_idx
                
        curr_start = curr_end = 0
        
        for char_idx in range(len(S)):
            last_val = last[S[char_idx]]
            curr_end = max(curr_end, last_val)
            
            if curr_end == char_idx:
                str_lens.append(curr_end - curr_start + 1)
                curr_start = cur_end = last_val + 1 
                
        return str_lens