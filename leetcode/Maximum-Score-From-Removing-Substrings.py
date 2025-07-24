#Tc: O(n)
#SC: O(n)  
'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
'''
from typing import List
class Solution:
    def stringRemove(self, s: str, pattern: str, xy: int) -> (str, int):
        """
        Removes all occurrences of the given 2-character pattern from the string `s`.
        Returns the updated string and the total points earned (xy for each removal).
        """
        if len(s) < 2:
            return s, 0  # No possible pattern to remove

        stack = []
        count = 0

        for ch in s:
            # Check if the top of the stack + current character matches the pattern
            if stack and ch == pattern[1] and stack[-1] == pattern[0]:
                stack.pop()       # Remove the matched pair
                count += xy       # Add points for this pattern
            else:
                stack.append(ch)  # Otherwise, keep building the string

        s = ''.join(stack)  # Build the updated string from stack
        return s, count      # Return new string and score from this pass

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Removes 'ab' and 'ba' substrings from `s` to maximize points.
        Always removes the higher-value pattern first.
        Returns total points earned.
        """
        points = 0

        # Remove pattern with higher value first to maximize score
        if x > y:
            s, gain = self.stringRemove(s, 'ab', x)
            points += gain
            s, gain = self.stringRemove(s, 'ba', y)
            points += gain
        else:
            s, gain = self.stringRemove(s, 'ba', y)
            points += gain
            s, gain = self.stringRemove(s, 'ab', x)
            points += gain

        return points
