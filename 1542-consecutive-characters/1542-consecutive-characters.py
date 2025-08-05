class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        max_c = 1

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                c = 1
            max_c = max(max_c,c)
        
        return max_c

        