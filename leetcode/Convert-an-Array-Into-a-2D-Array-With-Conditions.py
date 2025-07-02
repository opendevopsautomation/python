#Brute Force 
'''
Each iteration builds one row with all remaining numbers that haven't been repeated in that row.

It subtracts one occurrence from the frequency counter for each element added to the row.

It stops when all frequencies are zero.
'''
#TC: O(n)
#SC: O(n)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq={}
        result=[]
        for num in nums:
            # row=freq.get(num,0). # Default to 0 if num not in freq
            if num not in freq:
                freq[num] = 0
            row = freq[num]
            if len(result) == row:
                result.append([])
            result[row].append(num)
            # freq[num]=row+1  # Update count of how many times we've placed num
            freq[num] += 1
        return result        
