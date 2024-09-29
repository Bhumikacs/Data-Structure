import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx

class GraphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph GUI")
        self.root.state("zoomed")
        self.root.configure(bg="lightcoral")
        bgcolor = "lightcoral"
        font = "arial"
        fsize = 14

        # Configure the grid layout for the entire window
        self.root.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.graph = nx.Graph()

        # Add the new label for Graph Operations
        self.operations_label = tk.Label(root, text="Graph Operations", font=(font, fsize), bg=bgcolor)
        self.operations_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Create the input fields and buttons, aligned to the left side
        tk.Label(root, text="Vertex:", font=(font, fsize), bg=bgcolor).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.vertex_entry = tk.Entry(root, width=20)
        self.vertex_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.add_vertex_button = tk.Button(root, text="Add Vertex", font=(font, fsize), command=self.add_vertex)
        self.add_vertex_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # Move the "Remove Vertex" button next to the "Add Vertex" button
        self.remove_vertex_button = tk.Button(root, text="Remove Vertex", command=self.remove_vertex, font=(font, fsize))
        self.remove_vertex_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(root, text="Edge Vertex 1:", font=(font, fsize), bg=bgcolor).grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.edge_vertex1_entry = tk.Entry(root, width=20)
        self.edge_vertex1_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Label(root, text="Edge Vertex 2:", font=(font, fsize), bg=bgcolor).grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.edge_vertex2_entry = tk.Entry(root, width=20)
        self.edge_vertex2_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.add_edge_button = tk.Button(root, text="Add Edge", command=self.add_edge, font=(font, fsize))
        self.add_edge_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        self.remove_edge_button = tk.Button(root, text="Remove Edge", command=self.remove_edge, font=(font, fsize))
        self.remove_edge_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        self.display_graph_button = tk.Button(root, text="Display Graph", command=self.display_graph, font=(font, fsize))
        self.display_graph_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_node(vertex)
            self.vertex_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a vertex name")

    def remove_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex and vertex in self.graph.nodes:
            self.graph.remove_node(vertex)
            self.vertex_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Vertex not found")

    def add_edge(self):
        vertex1 = self.edge_vertex1_entry.get()
        vertex2 = self.edge_vertex2_entry.get()
        if vertex1 and vertex2 and vertex1 in self.graph.nodes and vertex2 in self.graph.nodes:
            self.graph.add_edge(vertex1, vertex2)
            self.edge_vertex1_entry.delete(0, tk.END)
            self.edge_vertex2_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Both vertices must exist")

    def remove_edge(self):
        vertex1 = self.edge_vertex1_entry.get()
        vertex2 = self.edge_vertex2_entry.get()
        if vertex1 and vertex2 and self.graph.has_edge(vertex1, vertex2):
            self.graph.remove_edge(vertex1, vertex2)
            self.edge_vertex1_entry.delete(0, tk.END)
            self.edge_vertex2_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Edge not found")

    def display_graph(self):
        plt.figure(figsize=(12, 6))  # Create a new figure with size 12x6
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=1000, font_size=14)
        plt.title("Graph Visualization")
        plt.show()  # Show the updated graph in a new window
    def create_new_window(self):
        self.destroy_window()  # Close the current window
        new_root = tk.Tk()
        new_app = GraphGUI(new_root)  # Create a new instance of the app
        new_root.attributes('-topmost', True)  # Bring new window to the front
        new_root.mainloop()

    def destroy_window(self):
        self.root.destroy()  # Close the current windo

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()
