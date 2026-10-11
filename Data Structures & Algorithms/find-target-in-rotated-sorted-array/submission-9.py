class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Pointers
        L = 0
        R = len(nums) - 1

        # Edge case: singleton
        if (len(nums) == 1):
            if nums[0] == target:
                return 0
            else:
                return -1

        # Step 1: Use a binary search to find the inflection point        
        while (L < R):
            mid = L + (R - L) // 2
            val = nums[mid]
            # If middle value is less than one on right
            if (nums[mid] < nums[R]):
                R = mid
            else:
                L = mid + 1

            print(mid)
        
        # This should have found the index of the minimum value
        inflection = L

        print(f'inflection = {inflection}')

        if (nums[inflection] == target):
            return inflection

        # Step 2: Split the array ihto two sorted sections,
        # performing binary search on each side
        array_1 = nums[:inflection]
        array_2 = nums[inflection:]

        L = 0
        R = len(array_1) 
        
        # Searching the left array
        while (L < R):
            mid = L + (R - L) // 2
            val = array_1[mid]

            if (val == target):
                return mid
            elif (val < target): # Cutting off bottom half
                L = mid + 1
            else:                # Cutting off top half
                R = mid

        
        # Searching the right array
        L = 0
        R = len(array_2)

        while (L < R):
            mid = L + (R - L) // 2
            val = array_2[mid]
            print(f'val = {val}')

            if (val == target): 
                return mid + len(array_1)
            elif (val < target): # Cutting off bottom half
                L = mid + 1
            else:                # Cutting off top half
                R = mid

        # Case that target is not in array
        return -1







        

        
        