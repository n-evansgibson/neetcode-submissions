class Solution:

    def topKFrequent_sorting(self, nums: List[int], k: int) -> List[int]:

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

    # Min-heap version
    def topKFrequent_minheap(self, nums: List[int], k: int) -> List[int]:

        # Create a hash map to store the count of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Create a minheap to put all the (count, num) pairs in
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            
            # If we go over k, then push out the lowest count
            if len(heap) > k:
                heapq.heappop(heap)

        # Add the remaining values in the minheap to the solution
        solution = []
        while len(solution) < k:
            solution.append(heapq.heappop(heap)[1])

        return solution

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create a hash map to store the frequency of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Create a list of groups to store each frequency
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)

        # Initialize an empty result list
        solution = []
        largest_frequency = len(freq) - 1

        # Loop from the largest possible frequency down to 1
        for i in range(largest_frequency, 0, -1):
            for num in freq[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution









        


        