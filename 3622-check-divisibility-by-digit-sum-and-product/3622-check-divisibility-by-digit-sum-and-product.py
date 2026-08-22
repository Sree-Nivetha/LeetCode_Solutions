class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        digitSum = 0
        digitPro = 1
        while (num!=0):
            temp = num % 10
            digitSum+=temp
            digitPro*=temp
            num//=10

        total = digitSum + digitPro
        if (n % total == 0):
            return True
        else:
            return False