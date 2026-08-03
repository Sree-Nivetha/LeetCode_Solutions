class Solution:
    def processStr(self, s: str) -> str:
        result=""
        for i in s:
            if i.isalpha() and i.islower():
                result+=i
            elif (i=="*"):
                if result is None:
                    continue
                else:
                    result=result[:-1]
            elif (i=="#"):
                result+=result
            elif (i=="%"):
                result=result[::-1]
            else:
                continue
        
        return result