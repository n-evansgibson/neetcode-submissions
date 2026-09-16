class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Combine the two arrays into one array of tuples
        total_length = len(position)
        cars = [(0,0)] * total_length
        for i in range(total_length):
            cars[i] = (position[i], speed[i])

        # Sort the array in descendinding order of position
        cars.sort(reverse=True)

        # Stack to sort fleets
        fleets = []

        # Iterate through the array
        for pos, speed in cars:

            # Compute time for car to reach the target
            time_to_target = (target - pos) / speed

            # Either join with fleet ahead or make a new fleet
            if (len(fleets) == 0 or time_to_target > fleets[-1]):

                # Creating a new fleet
                fleets.append(time_to_target)
            else:
                # Otherwise will be joined with new fleet 
                continue

        return len(fleets)

            

        


        
        