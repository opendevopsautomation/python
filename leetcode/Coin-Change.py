'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
#TC: O(amount * k), k is the number of different coins.
#SC: O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # If amount is 0, no coins are needed
        if amount == 0:
            return 0
        
        # Initialize DP array with 'inf', except min_coins_arr[0] = 0
        min_coins_arr = [0] + [float('inf')] * amount
        
        # Loop through all amounts from 1 to target amount
        for idx in range(1, amount + 1):
            # Try each coin to see if it can form the current amount
            for coin in coins:
                if coin <= idx:
                    min_coins_arr[idx] = min(min_coins_arr[idx], min_coins_arr[idx - coin] + 1)

        # If the target amount is still 'inf', it's impossible to form it, return -1
        return min_coins_arr[amount] if min_coins_arr[amount] != float('inf') else -1

#Reference: https://www.youtube.com/watch?v=NNcN5X1wsaw  
