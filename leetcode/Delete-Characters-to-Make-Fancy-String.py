'''
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
'''

#Approach: 1
#TC: O(n)
#SC: O(n)
from typing import List
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        left, right = 0, 1
        ans=[s[0]]
        while right < len(s):
            if s[left] == s[right]:
                # If the group is already 2 or more, skip the third
                if right - left >= 2:
                    right+=1
                    continue
                else:
                    ans.append(s[right])
            else:
                # Different character → reset the left pointer
                ans.append(s[right])
                left=right
            right+=1     
        return ''.join(ans)

#Approach: 2
#TC: O(n)
#SC: O(n)
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        ans = [s[0], s[1]]
        for idx in range(2,len(s)):
            if s[idx] == s[idx-1] and s[idx]==s[idx-2]:
                continue
            ans.append(s[idx])
        return ''.join(ans)