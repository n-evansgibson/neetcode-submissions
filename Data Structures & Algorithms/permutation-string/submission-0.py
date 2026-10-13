class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Edge cases
        if len(s1) > len(s2): return False

        # Create a reference dict
        reference = dict()
        for char in s1:
            reference[char] = reference.get(char, 0) + 1

        print(reference)

        # Define window
        window_size = len(s1)
        window = dict()
        curr_size = 0

        for i, char in enumerate(s2):
            # Add current value to hash
            window[char] = window.get(char, 0) + 1

            # If window has gotten too big, shrink it
            if i >= window_size:
                last_char = s2[i - window_size]
                window[last_char] -= 1
                if window[last_char] == 0:
                    del window[last_char]

            # Check for permutation
            if (reference == window): return True

        # Nothing found
        return False





        