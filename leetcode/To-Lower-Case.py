'''If the ASCII value of the character is between 65 and 90, character is "Upper".
If the ASCII value of the character is between 97 and 122, character is "Lower".
If the ASCII value of the character is between 48 and 57, character is "Number".
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=''
        for i in s:
            if (ord(i) >= 65 and ord(i) <= 90):
                       ans+=chr(ord(i)+32)
            else:
                       ans+=i
        return ans