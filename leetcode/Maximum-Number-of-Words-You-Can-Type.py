# Time: O(n + w × l) n = len(brokenLetters), w = number of words, l = avg word length
# Space: O(b) b = broken letters count
#Approach 1
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split(" ")
        blocked_count = 0

        for word in words:
            for ch in word:
                if ch in broken_set:
                    blocked_count += 1
                    break

        return len(words) - blocked_count

# Time: O(n + t), n = len(brokenLetters), t = len(text)
# Space: O(b) b = broken letters count
#Approach 2
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenmap = set(brokenLetters)
        result = len(text.split(" "))
        cantype = True
        for ch in text:
            if ch in brokenmap:
                cantype = False
            if ch == " " and not cantype:
                result -= 1
                cantype = True
        if not cantype:
            result -= 1
        return result
