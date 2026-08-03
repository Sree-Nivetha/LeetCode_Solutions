class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return True
        
        text=""
        for i in s:
            if i.isalnum():
                text=text+(i.lower())

        if (text==text[::-1]):
            return True
        else:
            return False