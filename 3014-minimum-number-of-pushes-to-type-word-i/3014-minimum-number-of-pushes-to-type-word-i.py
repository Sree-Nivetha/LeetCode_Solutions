class Solution:
    def minimumPushes(self, word: str) -> int:
        min_push = 0
        n = len(word)
        if (n<=8):
            return n
        else:
            count = 0
            while n > 7:
                count+=1
                n-=8
                min_push += (count * 8)

            min_push += (count+1) * n
            return min_push