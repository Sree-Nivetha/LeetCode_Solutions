class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * n
        cur = 0

        for i in range(n):
            ch = s[i]

            if 'a' <= ch <= 'z':
                cur += 1
            elif ch == '*':
                if cur > 0:
                    cur -= 1
            elif ch == '#':
                cur = min(cur * 2, 10**15)

            length[i] = cur

        if k >= cur:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if length[i] - 1 == k:
                    return ch
            elif ch == '#':
                prev = length[i] // 2
                if k >= prev:
                    k -= prev
            elif ch == '%':
                k = length[i] - 1 - k

        return '.'