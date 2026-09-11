import string

class Solution:
    def groupAnagrams_naive(self, strs: List[str]) -> List[List[str]]:

        # Creates list to store the solution
        solutionList = []

        # Creates a hash map to store all of the values
        solutionHash = {}

        # For each word, determine the anagram count and sort in hash
        for word in strs:
            # List will become key (initialize each section to 0)
            anagram_key = [0] * 26
            # Determine number of letters
            for i, letter in enumerate(string.ascii_lowercase):
                anagram_key[i] = word.count(letter)
            
            # Convert tuple for hashing
            key = tuple(anagram_key)

            # Check to see if the key is in the hash
            if key in solutionHash:
                solutionHash[key].append(word)
            # If not in the hash, create a new element: (key, [word])
            else:
                solutionHash[key] = [word]

        # After going through the entire list, turn values into a list
        solutionList = list(solutionHash.values())

        return solutionList


    # This version takes advantage of string sorting
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Note to self: defaultdict makes the default value a list here
        result = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            result[sorted_word].append(word)
        
        return list(result.values())



        



            

        

        


        