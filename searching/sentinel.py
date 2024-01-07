import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from runtime.time_measurement import time_function,  CodeTimer

#measure the line of code
with CodeTimer('Sentinel Linear Search'):
    for i in range(10):
        # 
        pass

class SentinelLinearSearch:
    def __init__(self, list):
        self.list = list

    @time_function
    def sentinel_linear_search(self, target):

        self.list[-1] += 1

        self.list[0] = target

        for i in range(len(self.list)):

            if self.list[i] == target:

                return i

        return -1

list = [5, 7, 12, 25, 30, 35]
sentinel_search = SentinelLinearSearch(list)
target = 25
index = sentinel_search.sentinel_linear_search(target)
print(f"The target value {target} is found at index {index}.")