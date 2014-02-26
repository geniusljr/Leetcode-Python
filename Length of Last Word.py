class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        a = s.split(" ")
        for i in range(len(a)-1, -1, -1):
            if len(a[i]) != 0:
                return len(a[i])
        return 0
