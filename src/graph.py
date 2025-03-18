import networkx as nx
import matplotlib.pyplot as plt

# 1. Membuat Graf
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)  
    return G

# 2. Degree Counting
def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree[node]

# 3. Path Finding/Tranversal
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.dfs_preorder_nodes(G, start))  

# 4. Fungsi untuk traversal menggunakan BFS
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_tree(G, start))  

# 5. Shortest Path
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source, target)  

# 6. Visualisasi Graf
def visualize_graph(G: nx.Graph):
    plt.figure(figsize=(6,6))  
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=12)
    plt.savefig("graph_visualization.png") 
    plt.show()  
