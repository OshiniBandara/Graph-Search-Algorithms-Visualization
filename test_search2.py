import sys
import networkx as nx
import matplotlib.pyplot as plt
import time
from queue import PriorityQueue, deque
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton,
    QComboBox, QTableWidget, QTableWidgetItem, QHBoxLayout
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Define Graph
G = nx.Graph()
edges = [
    ("Entrance", "Fruits", 1), ("Fruits", "Dairy", 1), ("Dairy", "Vegetables", 1),
    ("Vegetables", "Snacks", 1), ("Snacks", "Meat", 1), ("Snacks", "Noodles & Pasta", 1),
    ("Noodles & Pasta", "Fish", 1), ("Fish", "Frozen", 1), ("Frozen", "Bakery", 1),
    ("Bakery", "Health and Beauty", 1), ("Health and Beauty", "Pharmacy", 1),
    ("Pharmacy", "Spices", 1), ("Spices", "Drinks", 1), ("Drinks", "Entrance", 1),
    ("Spices", "Wine and Spirits", 1), ("Snacks", "Wine and Spirits", 1)
]
G.add_weighted_edges_from(edges)

# Search Algorithms
def bfs(graph, start, goal):
    start_time = time.time()
    visited, queue = set(), [[start]]
    nodes_explored = 0
    while queue:
        path = queue.pop(0)
        node = path[-1]
        nodes_explored += 1
        if node == goal:
            return path, time.time() - start_time, nodes_explored
        if node not in visited:
            visited.add(node)
            queue.extend([path + [neighbor] for neighbor in graph[node] if neighbor not in visited])
    return None, time.time() - start_time, nodes_explored

def dfs(graph, start, goal):
    start_time = time.time()
    stack, visited = [[start]], set()
    nodes_explored = 0
    while stack:
        path = stack.pop()
        node = path[-1]
        nodes_explored += 1
        if node == goal:
            return path, time.time() - start_time, nodes_explored
        if node not in visited:
            visited.add(node)
            stack.extend([path + [neighbor] for neighbor in graph[node] if neighbor not in visited])
    return None, time.time() - start_time, nodes_explored

def dijkstra(graph, start, goal):
    start_time = time.time()
    path = nx.shortest_path(graph, source=start, target=goal, weight='weight')
    return path, time.time() - start_time, len(path)

def ucs(graph, start, goal):
    start_time = time.time()
    queue = PriorityQueue()
    queue.put((0, [start]))
    visited = set()
    nodes_explored = 0
    while not queue.empty():
        cost, path = queue.get()
        node = path[-1]
        nodes_explored += 1
        if node == goal:
            return path, time.time() - start_time, nodes_explored
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.put((cost + 1, path + [neighbor]))
    return None, time.time() - start_time, nodes_explored

def dls(graph, start, goal, limit=3):
    def recursive_dls(node, path, depth):
        nonlocal nodes_explored
        nodes_explored += 1
        if node == goal:
            return path
        if depth == 0:
            return None
        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = recursive_dls(neighbor, path + [neighbor], depth - 1)
                if new_path:
                    return new_path
        return None
    
    start_time = time.time()
    nodes_explored = 0
    result = recursive_dls(start, [start], limit)
    return result, time.time() - start_time, nodes_explored

def ids(graph, start, goal, max_depth=5):
    for depth in range(max_depth):
        path, time_taken, nodes_explored = dls(graph, start, goal, depth)
        if path:
            return path, time_taken, nodes_explored
    return None, time.time() - start_time, 0

# GUI Class
class GraphSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Search Algorithms - PyQt6")
        self.setGeometry(100, 100, 1000, 800)
        self.initUI()
    
    def initUI(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        control_layout = QHBoxLayout()
        self.start_label = QLabel("Start:")
        self.start_node = QComboBox()
        self.start_node.addItems(G.nodes)
        self.end_label = QLabel("End:")
        self.end_node = QComboBox()
        self.end_node.addItems(G.nodes)
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.run_search)
        
        control_layout.addWidget(self.start_label)
        control_layout.addWidget(self.start_node)
        control_layout.addWidget(self.end_label)
        control_layout.addWidget(self.end_node)
        control_layout.addWidget(self.search_button)
        layout.addLayout(control_layout)
        
        self.result_table = QTableWidget()
        self.result_table.setColumnCount(4)
        self.result_table.setHorizontalHeaderLabels(["Algorithm", "Path", "Time (s)", "Nodes Explored"])
        layout.addWidget(self.result_table)
        
        self.canvas = FigureCanvas(plt.figure(figsize=(6, 6)))
        layout.addWidget(self.canvas)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def run_search(self):
        start = self.start_node.currentText()
        goal = self.end_node.currentText()
        
        algorithms = {
            "BFS": bfs,
            "DFS": dfs,
            "Dijkstra": dijkstra,
            "UCS": ucs,
            "DLS": dls,
            "IDS": ids
        }
        
        self.result_table.setRowCount(0)
        for idx, (alg, func) in enumerate(algorithms.items()):
            path, time_taken, nodes_explored = func(G, start, goal)
            if path:
                self.result_table.insertRow(idx)
                self.result_table.setItem(idx, 0, QTableWidgetItem(alg))
                self.result_table.setItem(idx, 1, QTableWidgetItem(" → ".join(path)))
                self.result_table.setItem(idx, 2, QTableWidgetItem(f"{time_taken:.6f}"))
                self.result_table.setItem(idx, 3, QTableWidgetItem(str(nodes_explored)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphSearchApp()
    window.show()
    sys.exit(app.exec())
