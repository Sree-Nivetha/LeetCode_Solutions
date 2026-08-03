# class Solution:
#     def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
#         gcdPairs=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 gcdPairs.append(math.gcd(nums[i],nums[j]))
        
#         gcdPairs.sort()
#         answer=[]
#         for i in range(len(queries)):
#             answer.append(gcdPairs[queries[i]])
        
#         return answer

class Solution:
    def gcdValues(self, A: list[int], queries: list[int]) -> list[int]:
        mx = max(A)
        freq = [0] * (mx + 1)
        for a in A: 
            freq[a] += 1
            
        GCD = [0] * (mx + 1)
        
        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            GCD[i] = sm * (sm - 1) // 2 - sum(GCD[i::i])
            
        GCD = list(accumulate(GCD))
        
        return [bisect.bisect_right(GCD, q) for q in queries]