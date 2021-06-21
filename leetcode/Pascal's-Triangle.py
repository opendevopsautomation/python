class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list=[]
        for i in range(numRows):
            list.append([1]*(i+1))
            if i>1:
                for j in range(1,i):
                    list[i][j]=list[i-1][j-1]+list[i-1][j]
        return list