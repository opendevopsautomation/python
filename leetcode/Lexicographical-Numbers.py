class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []         # This will store the final list of numbers
        curr = 1            # Start from 1

        for _ in range(n):  # Repeat n times to get n numbers
            result.append(curr)  # Add the current number to the result

            # If going deeper (like 1 → 10) is within limit, do it
            if curr * 10 <= n:
                curr *= 10
            else:
                # If current number is already at or beyond n, move up
                if curr >= n:
                    curr //= 10

                # Go to the next number (like 19 → 20)
                curr += 1

                # If the number ends with 0 (like 20, 30), remove the zero(s)
                # This helps move up in the number structure
                while curr % 10 == 0:
                    curr //= 10

        return result
