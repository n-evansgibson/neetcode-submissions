class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Create a hash set
        num_set = set(nums)
        longest_sequence = 0

        # Loop through entire set
        for num in num_set:
            # If n is the start of a sequence, start counting
            if (num-1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest_sequence = max(length, longest_sequence)
        return longest_sequence