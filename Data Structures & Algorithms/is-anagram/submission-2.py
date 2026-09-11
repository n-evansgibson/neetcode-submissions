class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Edge case: if both strings have the same length, return false
        if (len(s) != len(t)):
            return False

        # Create a hash map (dict) for each string
        hash_s = {}
        hash_t = {}

        # Put all of the elements into the set
        for letter in s:   
            # Count the frequency of each letter
            hash_s[letter] = hash_s.get(letter, 0) + 1

        for letter in t:
            # Count the frequency of each letter
            hash_t[letter] = hash_t.get(letter, 0) + 1
            
        # Test if the sets match
        return hash_s == hash_t




        