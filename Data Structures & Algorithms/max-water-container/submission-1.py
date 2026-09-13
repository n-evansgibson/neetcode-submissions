class Solution:
    def maxArea_naive(self, heights: List[int]) -> int:

        # Solution storage
        best_area = 0
        total_length = len(heights)

        # Two pointers
        L = 0
        
        # Starting with a brute force method. Loop through everything...
        for i in range(total_length):
            
            # Define pointers
            L = i + 1;

            while (L < total_length):

                # Calculate the area at that height
                width = abs(L - i)
                height = min(heights[L], heights[i])
                area = width * height

                # Check against current best area
                if (area > best_area):
                    best_area = area
 
                # Increment L pointer
                L += 1

        return best_area

    def maxArea(self, heights: List[int]) -> int:

        # Initialize pointers and solution
        best_area = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            best_area = max(area, best_area)

            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        return best_area






        