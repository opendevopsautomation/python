class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        print(set(candyType))
        return min(len(candyType) //2, len(set(candyType)))