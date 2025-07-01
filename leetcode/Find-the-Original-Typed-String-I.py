#TC: O(n)
#SC: O(1)
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=1  # Start with 1 because the first possibility is the whole word itself
        for idx in range(1,len(word)):
            # If consecutive characters are the same, it could have been a typo
            if word[idx-1]==word[idx]:
                ans+=1
        return ans
