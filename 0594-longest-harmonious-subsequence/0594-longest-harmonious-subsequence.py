class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_count=0
        for i in count:
            if i+1 in count:
                current_val=count[i]+count[i+1]
                max_count=max(max_count,current_val)

        return max_count