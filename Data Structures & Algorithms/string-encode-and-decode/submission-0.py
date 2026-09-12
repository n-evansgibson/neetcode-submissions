class Solution:

    # Note: I need to keep track of the length of each string, otherwise it will
    # be incredibly difficult to encode and decode where each string segment
    # begins and ends.

    # I will need to add a separator that sorts the length of the string

    # Example of ENCODED string: "XX_HelloXX_World", where XX is length of string

    def encode(self, strs: List[str]) -> str:

        parts = []

        # Iterate through each item in the list
        for s in strs:

            # Determine length of string to encode
            length = len(s)

            # Create encoded string for word
            encoded_str = str(length) + "_" + s

            # append to solution string
            parts.append(encoded_str)

        return "".join(parts)


    def decode(self, s: str) -> List[str]:

        solution = []
        encoded_len = len(s)
        pointer = 0

        while pointer < encoded_len:
           
           # Determine number of letters in the next encoded word
           string = s[pointer:encoded_len]
           count_index = string.find('_')
           letter_count = int(string[:count_index])

           # Find and add new string
           word_start = count_index + 1
           new_string = string[word_start: word_start + letter_count]
           solution.append(new_string)

           # Increment i based on letter count
           pointer = pointer + count_index + letter_count + 1

        return solution




