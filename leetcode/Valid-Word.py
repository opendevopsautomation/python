'''
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

 

Constraints:

1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
'''

#TC: O(n)
#SC: O(1)

class Solution:
    def isValid(self, word: str) -> bool:
        # Rule 1: The word must be at least 3 characters long
        if len(word) < 3:
            return False

        # Flags to check for at least one vowel and one consonant
        vowel = False
        consonant = False

        # Loop through each character in the word
        for ch in word:
            # Rule 2: The character must be a letter or a digit
            if not ch.isalnum():
                return False

            # Check only alphabetic characters for vowels/consonants
            if ch.isalpha():
                # Convert to lowercase to make the check case-insensitive
                if ch.lower() in 'aeiou':
                    vowel = True  # Found a vowel
                else:
                    consonant = True  # Found a consonant

        # Rule 3 & 4: Word must have at least one vowel and one consonant
        return vowel and consonant
