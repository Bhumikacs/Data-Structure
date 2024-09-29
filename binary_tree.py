import tkinter as tk
from tkinter import messagebox
from tkinter import font
# Class to create a new node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
# Class for binary tree operations
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    def _inorder_traversal(self, root, result):
        if root is not None:
            self._inorder_traversal(root.left, result)
            result.append(root.val)
            self._inorder_traversal(root.right, result)
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result
    def _preorder_traversal(self, root, result):
        if root is not None:
            result.append(root.val)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)
    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result
    def _postorder_traversal(self, root, result):
        if root is not None:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.val)
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node = self._get_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)
        return root
    def _get_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
# GUI class
class BinaryTreeGUI:
    def __init__(self, root):
        self.bt = BinaryTree()
        self.root = root
        self.root.title("Bhumika Shelar S113")
        self.root.configure(bg='#8F79A1')
        # Set full screen
        self.root.state('zoomed')
        # Define the font
        self.title_font = font.Font(family="Times New Roman", size=24)
        self.label_font = font.Font(family="Times New Roman", size=20)
        self.button_font = font.Font(family="Arial", size=16)
        # Label for Binary Tree Operations
        self.label = tk.Label(root, text="Binary Tree Operations",
                              font=self.title_font, bg="#8F79A1")
        self.label.grid(row=0, column=0, columnspan=2, pady=20)
        # Entry for inserting value
        self.entry = tk.Entry(root, font=self.label_font, width=15)
        self.entry.grid(row=2, column=0, padx=10, pady=10)
        # Button to insert value
        self.insert_button = tk.Button(root, text="Insert", font=self.button_font,
                                       command=self.insert_value, width=20)
        self.insert_button.grid(row=3, column=0, padx=10, pady=10)
        # Button to delete value
        self.delete_button = tk.Button(root, text="Delete", font=self.button_font,
                                       command=self.delete_value, width=20)
        self.delete_button.grid(row=4, column=0, padx=10, pady=10)
        # Button for in-order traversal
        self.inorder_button = tk.Button(root, text="In-order Traversal", font=self.button_font,
                                        command=self.inorder_traversal, width=20)
        self.inorder_button.grid(row=5, column=0, padx=10, pady=10)
        # Button for pre-order traversal
        self.preorder_button = tk.Button(root, text="Pre-order Traversal", font=self.button_font,
                                         command=self.preorder_traversal, width=20)
        self.preorder_button.grid(row=6, column=0, padx=10, pady=10)
        # Button for post-order traversal
        self.postorder_button = tk.Button(root, text="Post-order Traversal",                         font=self.button_font,
                                        command=self.postorder_traversal, width=20)
        self.postorder_button.grid(row=7, column=0, padx=10, pady=10)
        # Canvas to draw the tree structure
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.grid(row=2, column=1, rowspan=6, padx=20, pady=10)
    def insert_value(self):
        value = self.entry.get()
        if value.isdigit():
            self.bt.insert(int(value))
            messagebox.showinfo("Success", f"Value {value} inserted.")
            self.canvas.delete("all")  # Clear the previous drawing
            self.draw_tree()  # Draw the updated tree
        else:
            messagebox.showerror("Error", "Please enter a valid integer.")
    def delete_value(self):
        value = self.entry.get()
        if value.isdigit():
            self.bt.delete(int(value))
            messagebox.showinfo("Success", f"Value {value} deleted.")
            self.canvas.delete("all")  # Clear the previous drawing
            self.draw_tree()  # Draw the updated tree
        else:
            messagebox.showerror("Error", "Please enter a valid integer.")
    def inorder_traversal(self):
        result = self.bt.inorder_traversal()
        messagebox.showinfo("In-order Traversal", f"Result: {result}")
    def preorder_traversal(self):
        result = self.bt.preorder_traversal()
        messagebox.showinfo("Pre-order Traversal", f"Result: {result}")
    def postorder_traversal(self):
        result = self.bt.postorder_traversal()
        messagebox.showinfo("Post-order Traversal", f"Result: {result}")
    def draw_tree(self):
        if self.bt.root is not None:
            self._draw_tree(self.bt.root, 400, 50, 200)
    def _draw_tree(self, node, x, y, offset):
        if node.left:
            self.canvas.create_line(x, y, x - offset, y + 60, fill="black")
            self._draw_tree(node.left, x - offset, y + 60, offset // 2)
        if node.right:
            self.canvas.create_line(x, y, x + offset, y + 60, fill="black")
            self._draw_tree(node.right, x + offset, y + 60, offset // 2)
        self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="#8F79A1")
        self.canvas.create_text(x, y, text=str(node.val), fill="white", font=self.button_font)
    def create_new_window(self):
        self.destroy_window()  # Close the current window
        new_root = tk.Tk()
        new_app = BinaryTreeGUI(new_root)  # Create a new instance of the app
        new_root.attributes('-topmost', True)  # Bring new window to the front
        new_root.mainloop()

    def destroy_window(self):
        self.root.destroy()  # Close the current windo
# Main function to run the GUI
if __name__ == '__main__':
    root = tk.Tk()
    gui = BinaryTreeGUI(root)
    root.mainloop()
