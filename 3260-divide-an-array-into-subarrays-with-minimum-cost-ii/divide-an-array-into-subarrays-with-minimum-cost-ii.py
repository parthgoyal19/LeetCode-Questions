from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        n = len(nums)
        needed = k - 2  # Number of elements we need to pick from the window
        
        left_set = SortedList()   # Holds the 'needed' smallest elements
        right_set = SortedList()  # Holds the remaining elements in the window
        current_window_sum = 0
        
        # Helper function to add an element to our two-set system
        def add_element(val):
            nonlocal current_window_sum
            left_set.add(val)
            current_window_sum += val
            # If left_set exceeds the capacity, push the largest to right_set
            if len(left_set) > needed:
                largest = left_set.pop(-1)
                current_window_sum -= largest
                right_set.add(largest)
                
        # Helper function to remove an element from our two-set system
        def remove_element(val):
            nonlocal current_window_sum
            if val in right_set:
                right_set.remove(val)
            else:
                left_set.remove(val)
                current_window_sum -= val
                # If left_set is now under capacity, pull the smallest from right_set
                if right_set:
                    smallest = right_set.pop(0)
                    left_set.add(smallest)
                    current_window_sum += smallest

        # Step 1: Initialize the sliding window for the first possible second-subarray start (i1 = 1)
        # The valid window of elements to choose from is index range [2, 1 + dist]
        for idx in range(2, min(1 + dist + 1, n)):
            add_element(nums[idx])
            
        # Initial answer considers nums[0], nums[1] (as i1), and the best elements in the window
        min_total_cost = nums[0] + nums[1] + current_window_sum
        
        # Step 2: Slide the window by iterating through all possible positions for i1
        for i1 in range(2, n - needed):
            # Element leaving the window from the left edge
            # The old window was [i1, i1 + dist], so the element at i1 is no longer valid
            remove_element(nums[i1])
            
            # Element entering the window on the right edge
            new_idx = i1 + dist
            if new_idx < n:
                add_element(nums[new_idx])
                
            # Calculate total cost for the current choice of i1
            total_cost = nums[0] + nums[i1] + current_window_sum
            if total_cost < min_total_cost:
                min_total_cost = total_cost
                
        return min_total_cost