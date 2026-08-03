class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        least_comm=count.most_common()[:-3:-1]
        return [item[0] for item in least_comm]