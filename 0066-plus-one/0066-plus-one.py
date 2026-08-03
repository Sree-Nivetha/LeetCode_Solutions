class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit=0
        for i in digits:
            digit=digit*10 + i
        digit+=1
        result=[]
        while (digit!=0):
            num=digit%10
            result.insert(0,num)
            digit//=10

        return result