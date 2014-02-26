class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        i = len(s)-1
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                break;
        s = s[:(i+1)]
        i = len(s)-1
        spaceExist = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                spaceExist = True
                break;

        return len(s) if spaceExist==False else len(s)-i-1
            
            
