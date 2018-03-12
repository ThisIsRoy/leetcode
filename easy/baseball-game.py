class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for idx,op in enumerate(ops):
            if op == '+':
                last_two = self.last_valid_score(scores, 2)[0]
                scores.append(sum(last_two))
                
            elif op == 'D':
                last_one = self.last_valid_score(scores, 1)[0]
                scores.append(2 * last_one[0])
                
            elif op == 'C':
                last_idx = self.last_valid_score(scores, 1)[1][0]
                scores[last_idx] = None
                
            else:
                scores.append(int(op))
                
        score_sum = 0
        for val in scores:
            if val:
                score_sum += val
                
        return score_sum
                
    def last_valid_score(self, scores, num):
        val_score = [] 
        index = []
        idx = len(scores) - 1
        while len(val_score) < num:
            if scores[idx]:
                val_score.append(scores[idx])
                index.append(idx)
            
            idx -= 1
            
        return val_score, index