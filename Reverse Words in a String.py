class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        sArr, result = s.strip().split(" ")[::-1], ""
        for i in range(0, len(sArr)):
            if len(sArr[i]) != 0:
                result += sArr[i] + (" " if i != len(sArr)-1 else "")
        return result
