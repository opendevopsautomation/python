class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        dict_1={}
        ans=[]
        for i in range(len(pattern)):
            if pattern[i] in dict_1.keys():
                dict_1[pattern[i]].append(i)
            else:
                dict_1[pattern[i]]=[i]       
        for j in words:
            dict_2={}
            for k in range(0,len(j)):
                if j[k] in dict_2.keys():
                    dict_2[j[k]].append(k)
                else:
                    dict_2[j[k]]=[k]
            if list(dict_1.values()) == list(dict_2.values()):
                ans.append(j)
        return ans
#with function
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        def find(word):
            dict={}
            for i in range(len(word)):
                if word[i] in dict.keys():
                    dict[word[i]].append(i)
                else:
                    dict[word[i]]=[i]
            return dict
        dict_1=find(pattern)        
        for j in words:
            dict_2=find(j)
            if list(dict_1.values()) == list(dict_2.values()):
                ans.append(j)
        return ans