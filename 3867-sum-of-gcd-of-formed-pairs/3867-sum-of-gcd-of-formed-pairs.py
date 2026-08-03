class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        prefixGcd=[]
        mx=0
        for i in range(n):
            mx=max(mx,nums[i])
            prefixGcd.append(math.gcd(nums[i],mx))

        prefixGcd.sort()
        
        total=0
        left = 0
        right = n - 1
        
        while left < right:
            total += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return total