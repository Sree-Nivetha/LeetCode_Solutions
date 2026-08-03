class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos={'a':-1,'b':-1,'c':-1}
        count=0

        for i ,ch in enumerate (s):
            pos[ch]=i
            if pos['a']!=-1 and pos['b']!=-1 and pos['c']!=-1:
                count+=min(pos['a'],pos['b'],pos['c'])+1
        return count
