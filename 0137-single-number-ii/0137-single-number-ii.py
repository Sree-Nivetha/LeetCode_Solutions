class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        least_com=count.most_common()[-1][0]
        return least_com