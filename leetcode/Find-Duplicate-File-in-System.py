class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict={}
        for path in paths:
            dir=path.split(" ")
            rootpath=dir[0]
            for i in range(1,len(dir)):
                file=dir[0]+"/"+dir[i].split("(")[0]
                content=dir[i].split("(")[1][:-1]
                
                if content in dict.keys():
                    dict[content].append(file)
                else:
                    dict[content]=[file]
        ans=[]
        for i in dict:
            if len(dict[i]) > 1:
                ans.append(dict[i])
                
        return ans