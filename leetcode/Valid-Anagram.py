#Method 1:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s="".join(sorted(s))
        t="".join(sorted(t))
        if s == t:
            return True
        else:
            False

#Method 2:            
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1={}
        for i in s:
            if i in temp1.keys():
                temp1[i]+=1
            else:
                temp1[i]=1

        for j in t:
            if j not in temp1:
                return False    
            else:    
                temp1[j]-=1
        for k in temp1.values():
            if k != 0:
                return False
        return True            
                        