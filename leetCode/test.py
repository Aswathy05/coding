class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        for i in range(len(s)):
            if(s[i] not in dict):
                dict[s[i]]=1
            elif(s[i] in dict):
                dict[s[i]]+=1       
        for i in dict:
            if(dict[i]==1):
                for j in range(len(s)):
                    if(s[j]==i):
                        return(j) 
        else:
            return(-1)   
    print(firstUniqChar("leetcode"))