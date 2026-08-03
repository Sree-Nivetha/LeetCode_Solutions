# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer=[]
#         for temp in range(len(temperatures)):
#             count=0
#             for t in range(temp+1,len(temperatures)):  
#                 if (temperatures[t]>temperatures[temp]):
#                     count+=1
#                     break
#                 else:
#                     if (t==(len(temperatures)-1)):
#                         count=0
#                     else: 
#                         count+=1
#             answer.append(count)

#         return answer

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pre-allocate array with 0s to handle days with no future warmer temp
        answer = [0] * len(temperatures)
        stack = []  # Stores indices of the days
        
        for current_day, current_temp in enumerate(temperatures):
            # Check if current day is warmer than the days waiting in the stack
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = current_day - prev_day
            
            # Keep track of the current day's index
            stack.append(current_day)
            
        return answer
