from collections import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        avg_dict = defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue: 
            tree = queue.popleft()
            avg_dict[tree[1]].append(tree[0].val)
            
            if tree[0].left:
                queue.append((tree[0].left, tree[1] + 1))
            
            if tree[0].right:
                queue.append((tree[0].right, tree[1] + 1))
        
        avg_list = []
        for level in range(len(avg_dict.keys())):
            avg_list.append(float(sum(avg_dict[level])) / len(avg_dict[level]))
            
        return avg_list 
                
            
            