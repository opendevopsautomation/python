class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        temp_dict={'b':0,'a':0,'l':0,'o':0,'n':0}
        print(temp_dict)
        for s in range(len(text)):
            if text[s] in temp_dict:
                temp_dict[text[s]]+=1

        return min(temp_dict["b"],temp_dict["a"],temp_dict["l"]//2,temp_dict["o"]//2,temp_dict["n"])