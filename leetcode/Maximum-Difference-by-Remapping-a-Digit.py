#Time: O(n)
'''
for ch in s: scans the string once → O(n)
.replace(ch, '9') is also O(n) — it must scan the entire string
Total: 2 * O(n) → still O(n)
'''
#Space: O(n)  Creating a new string with replace()

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        for ch in s:
            if ch != "9":
                maxVal = int(s.replace(ch,"9"))
                break
            else:
                maxVal = int(s)
        minVal = int(s.replace(s[0],"0"))

        return maxVal - minVal 
