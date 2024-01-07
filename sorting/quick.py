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

def partition(array, little, big):

	pivot = array[big]
	i = little - 1

	for j in range(little, big):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[big]) = (array[big], array[i + 1])
	return i + 1

def quicksort(array, little, big):
	if little < big:
		pi = partition(array, little, big)
		quicksort(array, little, pi - 1)
		quicksort(array, pi + 1, big)

if __name__ == '__main__':
	array = [9,3,6,1,0,7,2,8]
	N = len(array)

	quicksort(array, 0, N - 1)
	print('Sorted array:')
	for x in array:
		print(x, end=" ")