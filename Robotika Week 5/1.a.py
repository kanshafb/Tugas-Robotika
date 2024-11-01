import heapq

def dijkstra_algorithm(graph, start, target):
    # Inisialisasi queue dan data jalur terpendek
    priority_queue = [(0, start, [])]
    visited = set()
    shortest_path_cost = {start: 0}

    while priority_queue:
        (current_cost, current_node, path) = heapq.heappop(priority_queue)
        
        # Jika sudah mencapai tujuan, kembalikan jalur dan biaya
        if current_node == target:
            return path + [current_node], current_cost
        
        # Jika sudah dikunjungi, lewati
        if current_node in visited:
            continue
        
        visited.add(current_node)
        path = path + [current_node]
        
        # Proses tetangga
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            new_cost = current_cost + weight
            if new_cost < shortest_path_cost.get(neighbor, float('inf')):
                shortest_path_cost[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor, path))

    return None, float('inf')

# Contoh graf
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 3, 'D': 7},
    'C': {'A': 5, 'B': 3, 'D': 1},
    'D': {'B': 7, 'C': 1}
}

# Eksekusi
start_node, target_node = 'A', 'D'
path, cost = dijkstra_algorithm(graph, start_node, target_node)
print(f"Jalur terpendek: {path} dengan biaya: {cost}")
