class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result=[]
        q=deque(range(1,9))
        while q:
            n=q.popleft()
            if n>high:
                continue
            if low<=n<=high:
                result.append(n)
            ones=n%10
            if ones<9:
                q.append(n*10+(ones+1))
        return result