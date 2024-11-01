import heapq
import math

def heuristic(node1, node2):
    # Menghitung jarak Euclidean sebagai heuristic
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)

def a_star_algorithm(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    visited = set()
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            # Kembali ke jalur jika sampai di tujuan
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        visited.add(current)
        
        # Tetangga (atas, bawah, kiri, kanan)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g_score[current] + 1
                if neighbor in visited and tentative_g >= g_score.get(neighbor, float('inf')):
                    continue
                
                if tentative_g < g_score.get(neighbor, float('inf')) or neighbor not in [i[1] for i in open_list]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None

# Contoh grid dengan rintangan
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Eksekusi
start, goal = (0, 0), (4, 4)
path = a_star_algorithm(grid, start, goal)
print(f"Jalur A*: {path}")
