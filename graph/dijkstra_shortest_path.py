import sys
import os
import heapq
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from runtime.time_measurement import time_function,  CodeTimer
with CodeTimer('LS24'):
    for i in range(10):
        pass

from typing import List

class graph():
    @time_function
    def dijkstra(graph, start):
        jarak = {node: float('infinity') for node in graph}
        jarak[start] = 0
        antrian_prioritas = [(0, start)]

        while antrian_prioritas:
            jarak_sekarang, node_sekarang = heapq.heappop(antrian_prioritas)

            if jarak_sekarang > jarak[node_sekarang]:
                continue

            for tetangga, bobot in graph[node_sekarang].items():
                jarak_baru = jarak_sekarang + bobot

                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru
                    heapq.heappush(antrian_prioritas, (jarak_baru, tetangga))

        return jarak

    graf = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    node_awal = 'A'
    jalur_terpendek = dijkstra(graf, node_awal)

    print(f"Jarak terpendek dari node {node_awal}: {jalur_terpendek}")
