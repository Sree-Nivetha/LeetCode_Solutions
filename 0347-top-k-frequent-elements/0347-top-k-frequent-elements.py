class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        most_com=count.most_common(k)
        result=[most_com[i][0] for i in range(len(most_com))]
        return result