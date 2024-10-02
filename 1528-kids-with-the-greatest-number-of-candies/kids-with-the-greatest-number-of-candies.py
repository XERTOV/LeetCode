class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res =[]

        for i in candies:
           res.append(i + extraCandies >= max_candies) 
                
        return res
        