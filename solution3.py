from typing import List

# Runtime = 203 ms

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        # Check the first element between original list
        # and temp list (with new values)
        def checkFirstElement(i, j, n, size, temp):
            if i < n:
                first = nums[i]
                if j < size and temp[j] < first:
                    first = temp[j]
                    j += 1
                else:
                    i += 1
            else:
                first = temp[j]
                j += 1
            return i, j, first
        count, temp = 0, []
        n, i, j, size = len(nums), 0, 0, 0

        nums.sort()
        while (n-i + size-j) >= 2:
            # Check first min value
            i, j, first = checkFirstElement(i, j, n, size, temp)

            # Break if the first element from sorted list 
            # is greater than or equal to k
            if first >= k:
                break

            # Check second min value
            i, j, second = checkFirstElement(i, j, n, size, temp)

            # Append new value in temp
            temp.append( (min(first, second)*2) + max(first, second) )

            # Update temp size and operation count
            size, count = size+1, count+1
        return count