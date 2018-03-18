class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        
        poison = [[timeSeries[0], timeSeries[0] + duration]]
        
        for time in timeSeries[1:]:
            if time > poison[-1][1]:
                poison.append([time, time + duration])
                
            else:
                poison[-1][1] = time + duration
                
        poison_time = 0
        
        for interval in poison:
            poison_time += interval[1] - interval[0]
            
        return poison_time
        