from Graf import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

# 1. Membuat graf
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5), (5, 6)]
G = create_graph(edges)

# 2. Menampilkan simpul dan sisi dalam graf
print("Simpul:", list(G.nodes))
print("Sisi dalam:", list(G.edges))

# 3. Menghitung derajat suatu simpul
node = 5
degree = get_degree(G, node)
print(f"Derajat simpul {node}: {degree}")

# 4. DFS Traversal dari simpul tertentu
start_node = 1
dfs_result = dfs_traversal(G, start_node)
print(f"DFS traversal dari simpul {start_node}: {dfs_result}")

# 5. BFS Traversal dari simpul tertentu
bfs_result = bfs_traversal(G, start_node)
print(f"BFS traversal dari simpul {start_node}: {bfs_result}")

# 6. Menemukan jalur terpendek antara dua simpul
source, target = 1, 6
shortest_path = find_shortest_path(G, source, target)
print(f"Jalur terpendek dari {source} ke {target}: {shortest_path}")

# 7. Visualisasi graf
visualize_graph(G)
