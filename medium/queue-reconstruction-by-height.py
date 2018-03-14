# Used greedy algorithm to sort and insert
# Super interesting problem

from collections import defaultdict

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return []
        
        order_dict = defaultdict(lambda: False)
        idx = 1
        
        order_list = []
        
        # sorts people into lists of the same height
        for person in people:
            height = person[0]
            if not order_dict[height]:
                order_dict[height] = idx
                order_list.append([person])
                idx += 1
                    
            else:
                order_list[order_dict[height] - 1].append(person)
                
        # sorts people within the height groups
        for idx in range(len(order_list)):
            order_list[idx].sort(key = lambda x: x[1])
            
        order_list.sort(key = lambda x: x[0], reverse = True)    
            
        queue = order_list.pop(0)
        sorted_people = [item for sublist in order_list for item in sublist]
        
        for tup in sorted_people:
            queue.insert(tup[1], tup)
                
        return queue
        