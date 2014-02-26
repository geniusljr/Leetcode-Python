class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        a = []
        a.append(True)
        for i in range(1, len(s)+1):
            success = False
            for j in range(i-1, -1, -1):
                if a[j] and (s[j:i] in dict):
                    success = True
                    a.append(True)
                    break
            if success == False:
                a.append(False)
        return a[len(s)]
