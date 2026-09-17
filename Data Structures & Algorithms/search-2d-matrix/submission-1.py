class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Combine into one larger list
        bank = []
        for row in matrix:
            bank.extend(row)

        print(bank)

        # Implement normal binary search
        L = 0
        R = len(bank) - 1

        while L <= R:
            
            mid = (L + R) // 2
            val = bank[mid]

            if (target > val):
                L = mid + 1
            elif (target < val):
                R = mid - 1
            else:
                return True

        return False

        
        