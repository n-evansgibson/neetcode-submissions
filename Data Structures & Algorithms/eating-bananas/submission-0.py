class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Determine the maximum value of k
        max_k = max(piles)

        # Compute binary search
        L = 1
        R = max_k
        result = max_k

        while (L <= R):

            # Calculate current speed to test
            curr_k = (L + R) // 2

            # See if the speed will work
            eating_time = 0
            for pile in piles:
                eating_time += math.ceil(float(pile) / curr_k)

            # If total hours is within allowed time, record
            if (eating_time <= h):
                result = curr_k
                R = curr_k - 1
            else:
                L = curr_k + 1
        
        # Return the smallest valid speed that was found
        return result






    
        