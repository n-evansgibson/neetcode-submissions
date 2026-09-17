class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Perform binary search on array
        L = 0
        R = len(nums) - 1

        # Edge cases
        if (len(nums) == 1) or (nums[-1] > nums[0]):
            return nums[0]
        
        # From here we are guaranteed that the array is rotated
        while (L < R):

            mid = L + (R- L) // 2
            val = nums[mid]

            # Case 1: Answer is on the left
            if nums[mid] < nums[R]:
                R = mid
            else:
                # Case 2: value is on the right
                L = mid + 1
        return nums[L]
            




        