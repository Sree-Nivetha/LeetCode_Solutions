class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res_lst=[]
        for i in range(1,n+1):
            if (i%3==0 and i%5==0):
                res_lst.append("FizzBuzz")
            elif (i%3==0):
                res_lst.append("Fizz")
            elif (i%5==0):
                res_lst.append("Buzz")
            else:
                res_lst.append(str(i))

        return res_lst
        