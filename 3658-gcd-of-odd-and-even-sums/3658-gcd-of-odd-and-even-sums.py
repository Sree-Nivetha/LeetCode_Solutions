class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(oddNum, evenNum):
            if (oddNum % evenNum==0):
                return evenNum
            return gcd(evenNum, oddNum%evenNum)

        sumOdd=0
        sumEven=0
        for i in range(1,(n*2)+1):
            if (i%2==0):
                sumEven+=i
            else:
                sumOdd+=i
        return gcd(sumOdd,sumEven)   