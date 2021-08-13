#TC=nlogn
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()   #Sort the array
        tmp_dct={}
        for i in arr:    #Create a dictionary with the count of element
            if i in tmp_dct.keys():
                tmp_dct[i]+=1
            else:
                tmp_dct[i]=1
        #Iterate the array and divide it with 2 in case of -ve value otherwise multiply with 2                
        for j in arr:   
            if tmp_dct[j] == 0:
                continue
            tmp=j//2 if j < 0 else j*2
        #Return False in case element of the array is -ve, even not divisble by 0 or computed value at 15 not in dictionary's key 
            if (j < 0 and j %2 != 0) or tmp not in tmp_dct:   
                return False
            if tmp_dct[j] > tmp_dct[tmp]:
                return False
            else:                
                tmp_dct[j]-=1
                tmp_dct[tmp]-=1

        return True