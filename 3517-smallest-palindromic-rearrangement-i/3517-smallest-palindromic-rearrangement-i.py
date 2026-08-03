class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if s is None or len(s)==1:
            return s

        n=len(s)
        result=""
        if (n % 2 == 0):        
            text = "".join(sorted(s[0:n//2])) 
            result+=text
            return result + result[::-1]
        else:
            text = "".join(sorted(s[0:n//2])) 
            result+=text
            return result + s[n//2] + result[::-1]