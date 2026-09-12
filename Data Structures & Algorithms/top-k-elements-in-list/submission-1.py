class Solution:
    def topKFrequent_naive(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Determine the frequency of each value in the array
        length = len(nums)
        frequency_dict = defaultdict(list)
        solution = []
        
        for index in range(0, length):
            
            # Get the count of that number
            count = nums.count(nums[index])

            # Add the current value to the frequency count
            if nums[index] not in frequency_dict[count]:
                frequency_dict[count].append(nums[index])
            
        # Step 2: Sort the keys by frequency
        frequency_list = sorted(list(frequency_dict))
        freq_list_len = len(frequency_list)
        
        # Step 3: Take the k greatest values from the top of the sorted list
        index = 0
        while len(solution) < k:
            
            # Add top frequencies to list
            top_index = freq_list_len - index - 1
            kth_frequency = frequency_list[top_index]
            kth_value = frequency_dict[kth_frequency]
            solution.extend(kth_value)

            # Increment index
            index = index + 1
             

        # Step 4: Return the completed list
        return solution

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create a hash map to store the count of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Convert to a list that can be sorted by frequency
        count_array = []
        for  num, cnt in count.items():
            count_array.append([cnt, num])

        # Sorts by frequency
        count_array.sort()

        # Pops off the k highest frequencies from the sorted list
        solution = []
        while len(solution) < k:
            # Only add the value
            solution.append(count_array.pop()[1])

        return solution



        


        