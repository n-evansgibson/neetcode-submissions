class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Define pointers
        L = 0 
        R = len(nums) - 1

        # Repeat the algorithm until we have searched the whole array
        while L <= R:

            # Calculate midpoint
            mid = (R + L) // 2
            val = nums[mid]

            if target > val:
                L = mid + 1
            elif target < val:
                R = mid - 1
            else:
                return mid

        return -1

        