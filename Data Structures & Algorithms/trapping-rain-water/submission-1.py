class Solution:
    def trap(self, height: List[int]) -> int:

        # Note: This is very similar to the max area problem, except
        # we need to take into account a couple of important factors.

        # Edge cases
        total_length = len(height)
        if total_length <= 2: return 0

        # Output
        total_water = 0

        # Create prefix and suffix maximum arrays
        prefix_max_array = [0] * total_length
        suffix_max_array = [0] * total_length

        # Calculate prefix and suffix max array
        curr_prefix_max = 0
        curr_suffix_max = 0

        for i in range(total_length):

            # Prefix max array
            curr_val = height[i]
            if (curr_val > curr_prefix_max):
                curr_prefix_max = curr_val
            prefix_max_array[i] = curr_prefix_max

            # Suffix max array
            suffix_i = total_length - 1 - i
            curr_val_s = height[suffix_i]
            if (curr_val_s > curr_suffix_max):
                curr_suffix_max = curr_val_s
            suffix_max_array[suffix_i] = curr_suffix_max

        # Iterate to find trapped water at each position
        for pos in range(total_length):
            trapped_water = min(prefix_max_array[pos], suffix_max_array[pos]) - height[pos]
            total_water += trapped_water

        return total_water



            


        




        
        