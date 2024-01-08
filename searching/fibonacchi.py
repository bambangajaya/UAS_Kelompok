import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from runtime.time_measurement import time_function,  CodeTimer
with CodeTimer('LS24'):
    for i in range(10):
        pass

from typing import List


class FibonacchiSearch():
    @time_function 
    def fibonacci_search(lst, target):
        size = len(lst)
        start = -1
        f0 = 0
        f1 = 1
        f2 = 1
        
        while(f2 < size):
            f0 = f1
            f1 = f2
            f2 = f1 + f0
        
        while(f2 > 1):
            index = min(start + f0, size - 1)
            if(lst[index] < target):
                f2 = f1
                f1 = f0
                f0 = f2 - f1
                start = index
            elif(lst[index] > target):
                f2 = f0
                f1 = f1 - f0
                f0 = f2 - f1
            else:
                return index
        
        if(f1 and lst[start + 1] == target):
            return start + 1
        else:
            return -1
        
    lst = [1, 3, 5, 7, 9]
    target = 5
    result = fibonacci_search(lst, target)
    if(result == -1):
        print("Elemen tidak ditemukan")
    else:
        print("Elemen ditemukan pada indeks ke", result)