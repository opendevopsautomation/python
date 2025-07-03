#TC: O(k^2)
#SC: O(k)
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        
        while len(word) < k:
            for ch in word:
                # Move to next character, wrap from 'z' to 'a'
                word = word + chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
                '''
                Sample 
                ch = 'a'
                ord('a') = 97
                ord('a') - ord('a') = 0
                0 + 1 = 1
                1 % 26 = 1
                1 + ord('a') = 98
                chr(98) = 'b'
                  '''        
        return word[k - 1]
