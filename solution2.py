from typing import List
import heapq

# Runtime = 268 ms

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
    # Convert the list into a min-heap
    heapq.heapify(nums)
    count = 0
    
    while nums[0] < k:
        if len(nums) < 2:
            # If there are less than 2 elements, we cannot perform the operation
            break
        
        # Extract the two smallest elements
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        
        # Apply the operation
        new_element = min(x, y) * 2 + max(x, y)
        
        # Insert the new element back into the heap
        #        while maintaining the heap order
        heapq.heappush(nums, new_element)
        
        # Increment the operation count
        count += 1
    
    return count