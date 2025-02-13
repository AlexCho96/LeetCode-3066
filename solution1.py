from typing import List

# Time Limit Exceeded - 669/675 testcase
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        
        while True:
            nums.sort()
            if len(nums) < 2 or nums[0] >= k:
                break
            x = nums.pop(0)
            y = nums.pop(0)
            
            new_element = min(x, y) * 2 + max(x, y)
            nums.append(new_element)
            count += 1
        
        return count