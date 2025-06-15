#Time Complexity - O(n)
'''
str(num)	O(n)	Convert integer to string, where n is the number of digits
for ch in s	O(n)	Scans each digit to find one to replace
s.replace(...)	O(n)	Replaces all occurrences of one digit (string operation)
int(...)	O(n)	Converting result back to integer
'''
#Space Complexity - O(n)

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Create max number by replacing the first non-9 digit with 9
        for ch in s:
            if ch != '9':
                maxVal = int(s.replace(ch,'9'))
                break
            else:
                maxVal = int(s)

        # Create min number
        if s[0] != '1':
            minVal = int(s.replace(s[0],'1'))
        else:
            for ch in s[1:]:
                if ch not in {'0', '1'}:
                    minVal = int(s.replace(ch,'0'))
                    break
                else:
                    minVal = int(s)
        return maxVal - minVal
