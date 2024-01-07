import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from runtime.time_measurement import time_function,  CodeTimer
#measure the line of code
with CodeTimer('bebas buat penanda'):
    for i in range(10):
        #do something
        pass
#measure function
@time_function   
def search():
   pass

class binarysearch:
    def binary_search(self, nums: list[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1





bs = binarysearch()

nums = [2, 3, 4, 10, 40]
target = 4
index = bs.binary_search(nums, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the list")