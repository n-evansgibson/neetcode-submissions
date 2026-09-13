class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # We have that the array is sorted, therefore we can use two pointers.
        L = 0
        R = len(numbers) - 1

        while (L < R):
            
            sum = numbers[L] + numbers[R]
            # If the numbers match, return the pair
            if (sum == target):
                return [L + 1, R + 1]
            elif (sum < target):
                L += 1
            elif (sum > target):
                R -= 1
            
        