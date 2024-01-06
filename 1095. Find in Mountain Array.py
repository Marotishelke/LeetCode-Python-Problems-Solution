# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        # Find the index of the peak element from the mountain array
        peak_index = self.find_peak_index(1, length - 2, mountain_arr)

        # Binaray search for the target in the increasing sequence of the arr
        increasing_index = self.binary_search(0, peak_index, target, mountain_arr, False)
        if mountain_arr.get(increasing_index) == target:
            return increasing_index # Target found in the increasing part
        
        # Binary search for the target in the decreasing sequence of the arr
        decreasing_index = self.binary_search(peak_index + 1, length - 1, target, mountain_arr, True)
        if mountain_arr.get(decreasing_index) == target:
            return decreasing_index # Target found in the decreasing sequence
        
        return -1 # Target not found in the mountain array

    # Function for finding the peak element's index from the array
    def find_peak_index(self, low, high, mountainArr):
        while(low != high):
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1 # Move to the left side
            else:
                high = mid # Move to the right side
        return low # Return the index of the peak element
    
    def binary_search(self, low, high, target, mountain_arr, reversed):
        while(low < high):
            mid = low + (high - low) // 2
            if reversed:
                if mountain_arr.get(mid) > target:
                    low = mid + 1 # Move to the right side 
                else:
                    high = mid # Move to the left side
            else:
                if mountain_arr.get(mid) < target:
                    low = mid + 1 # Move to the right side
                else:
                    high = mid # Move to the left side
                
        return low # Return the index of the target 
        
