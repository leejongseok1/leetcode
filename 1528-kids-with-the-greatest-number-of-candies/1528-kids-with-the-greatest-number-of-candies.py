class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        results = []
        max_candy = max(candies)

        for candy in candies:
            results.append(candy + extraCandies >= max_candy)

        return results
