class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0]<=prev[1]:
                prev[1] = max(prev[1],interval[1])
            else:
                merged.append(prev)
                prev =interval
        
        merged.append(prev)
        return merged

            
    
        
        
        #we will sort them by last index
        # [1,3].[2,6],[8,10].[15,18]
        # check if firtin<=last ind min of 2 and max of 2 
        
      
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

        