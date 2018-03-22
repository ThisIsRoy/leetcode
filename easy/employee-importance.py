"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employ_dict = dict()
        
        # create a dictionary of id to employee info
        for employee in employees:
            employ_dict[employee.id] = (employee.importance, employee.subordinates)
        
        # modified bfs
        queue = [id]
        score = 0
        while queue:
            curr_id = queue.pop(0)
            score += employ_dict[curr_id][0]
            queue += employ_dict[curr_id][1]
                
        return score
        