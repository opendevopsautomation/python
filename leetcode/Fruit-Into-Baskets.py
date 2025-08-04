
#TC: O(n)
#SC: O(n)
#https://www.youtube.com/watch?v=Oi09pnLLy78&ab_channel=NikhilLohia
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruits = 0
        basket = {}  # Stores count of fruit types in the current window

        for right in range(len(fruits)):
            # Add current fruit to the basket
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # Shrink window if more than 2 fruit types
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1  # Move left pointer to reduce fruit types

            # Update max fruits collected
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
