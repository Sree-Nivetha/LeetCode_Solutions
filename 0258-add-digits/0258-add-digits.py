class Solution:
    def addDigits(self, num: int) -> int:
        def add(n):
            total=0
            while(n!=0):
                total+=n%10
                n=n//10

            if (total>=10):
                return add(total)
            else:
                return total
        if (num>=10):
            return add(num)
        else:
            return num