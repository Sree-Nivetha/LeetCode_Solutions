class Solution:
    def maxProduct(self, n: int) -> int:
        digits=[]
        while n>0:
            num = n%10
            digits.append(num)
            n//=10
        
        m = len(digits)
        max_p =0
        for i in range(m):
            for j in range(i+1,m):
                product = digits[i] * digits[j]
                max_p = max_p if max_p>product else product
        return max_p