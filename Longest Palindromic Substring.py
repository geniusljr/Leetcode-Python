class Solution:
    # @return a string

    def process(self, s):
        ret = "^"
        for i in range(0, len(s)):
            ret += "#" + s[i]
        ret += "#$"
        return ret

    def longestPalindrome(self, s):
        T = self.process(s)
        C = 0
        R = 0
        P = [0 for i in range(0, len(T))]
        for i in range(1, len(T)-1):
            i_mirror = 2*C-i
            P[i] = min(R-i, P[i_mirror]) if R > i else 0
            while T[i+1+P[i]] == T[i-1-P[i]]:
                P[i] = P[i]+1

            if i+P[i] > R:
                C = i
                R = i+P[i]

        maxLen = 0
        centerIndex = 0
        for i in range(1, len(T)-1):
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i

        return s[(centerIndex-1-maxLen)/2: (centerIndex-1-maxLen)/2+maxLen]
            
