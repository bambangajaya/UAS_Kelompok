import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from runtime.time_measurement import time_function,  CodeTimer

#measure the line of code
with CodeTimer('Bubble Sort'):
    for i in range(10):
        # 
        pass

class BubbleSort:
    def __init__(self, numbers):
        self.numbers = numbers

    @time_function
    def bubble_sort(self):

        swapped = True

        while swapped:
            swapped = False

            for i in range(len(self.numbers) - 1):

                if self.numbers[i] > self.numbers[i + 1]:

                    self.numbers[i], self.numbers[i + 1] = self.numbers[i + 1], self.numbers[i]

                    swapped = True

        return self.numbers

unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original unsorted list:", unsorted_numbers)

sorter = BubbleSort(unsorted_numbers)
sorted_numbers = sorter.bubble_sort()
print("Sorted list:", sorted_numbers)