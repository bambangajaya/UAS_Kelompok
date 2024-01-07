import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from runtime.time_measurement import time_function,  CodeTimer
with CodeTimer('devide and congquer'):
    for i in range(10):

        pass 

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

@time_function  
def closest_pair_of_points(points):
    closest_pair = None
    closest_distance = float('inf')

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            if distance < closest_distance:
                closest_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, closest_distance
points = [(2, 3), (4, 8), (6, 2), (9, 8), (1, 1)]
closest_pair, distance = closest_pair_of_points(points)
print(f"The closest pair of points is: {closest_pair}")
print(f"The distance between these points is: {distance}")