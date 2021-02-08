class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left=[]
        right=[]
        result=[]
        temp=math.inf
        for i in range(len(s)):
            if s[i] ==c:
                temp=0
            left.append(temp)
            temp+=1 
        temp=math.inf            
        for j in range(len(s)-1,-1,-1): 
            if s[j]==c:
                temp=0
            right.insert(0,temp)
            temp+=1 
        for k in range(len(s)):
            result.append(min(left[k],right[k]))
        return result    
                
        

#2 method
class Solution:
    def right(self,r,c):
        ans=math.inf
        i=0
        if c in r:
            while i < len(r):
                if r[i] ==c:
                    return i+1
                i+=1
        return ans    
    def left(self, l,c):
        ans=math.inf
        j=len(l)-1
        if c in l:
            while j >=0:
                if l[j]==c:
                    return len(l)-j
                j-=1
        return ans   
    
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result=[]
        for i in range(len(s)):
            if s[i]==c:
                result.append(0)
            else:   
                result.append(min(self.right(s[i+1:],c),self.left(s[:i],c)))
        return result               

#3rd method
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                ans.append(i)
        res = []
        for j in range(len(s)):
            temp=math.inf
            for i in ans:
                temp=(min(temp,abs(j-i)))
               
            res.append(temp)
            
        return res
                
        