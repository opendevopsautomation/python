class Solution:
    #TC : O(n2)
    #SC : O(n)  
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dict={}
        for i in (arr):
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1  
        result=0        
        for i in (dict):
            for j in (dict):
                k=target-i-j
                if k in dict.keys():
                    freq1=dict[i]
                    freq2=dict[j]
                    freq3=dict[k]
                    if (i ==j and i==k):                             #freq1C3
                        result+=((freq1)*(freq1-1)*(freq1-2))//6     
                    elif (i==j and i!=k):                            #freq1C2*freq3C1
                        result+=((freq1)*(freq1-1))//2*freq3
                    elif(i<j and j< k):                              #freq1C1*freq2C1*freq3C1
                        result+=((freq1*freq2*freq3))
            result=result% (10**9 + 7)
        return int(result)            