import tkinter as tk
from tkinter import messagebox,simpledialog
from tkinter import Label,Entry,Button
from priority_queue import PriorityQueueApp
from binary_tree import BinaryTreeGUI
from huffman_coding import HuffmanCodingApp
from graph import GraphGUI
from travelling_salesman_problem import TSPGUI
from hashtable import gui
from stack_list import StackGUI
from single_linked_list import LinkedListApp
class ButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Structures and Algorithms")
        self.root.configure(bg='lightblue')
        self.root.geometry("800x600")  # Increased size for better UI

        # Button names as per your requirements
        button_names = [
            "Stack",
            "Single Linked List",
            "Doubly Linked List",
            "Queue",
            "Priority Queue",
            "Binary Tree",
            "Huffman Coding",
            "Graph",
            "Travelling Salesman Problem",
            "Hashtable",
        ]

        # Create buttons
        for i, name in enumerate(button_names):
            button = tk.Button(self.root, text=name, command=lambda i=i: self.on_button_click(i), width=20, height=3, bg='white', fg='black', font=("Helvetica", 12, "bold"))
            button.grid(row=i // 3, column=i % 3, padx=10, pady=10, ipadx=5, ipady=5, sticky="nsew")

        # Configure grid to be responsive
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
            self.root.rowconfigure(i, weight=1)

    def on_button_click(self, button_number):
        if button_number == 0:  # Stack button
             app =StackGUI(root)  # Create an instance of the app
             app.create_new_window()  # This will close the current window and open a new one
             root.mainloop()# This will close the current window and open a new one
             root.mainloop()
        elif button_number == 1:  # Single Linked List button
             app =LinkedListApp(root)  # Create an instance of the app
             app.create_new_window()  # This will close the current window and open a new one
             root.mainloop()# This will close the current window and open a new one
             root.mainloop()
        elif button_number == 2:  # Doubly Linked List button
            self.run_doubly_linked_list_app()
        elif button_number == 3:  # Queue button
            self.run_queue_app()
        elif button_number == 4:  # Queue button
            app = PriorityQueueApp(root)  # Create an instance of the app
            app.create_new_window()  # This will close the current window and open a new one
            root.mainloop()
        elif button_number == 5:
            app = BinaryTreeGUI(root)  # Create an instance of the app
            app.create_new_window()  # This will close the current window and open a new one
            root.mainloop()
        elif button_number == 6:
            app =HuffmanCodingApp(root)  # Create an instance of the app
            app.create_new_window()  # This will close the current window and open a new one
            root.mainloop()
        elif button_number == 7:
            app =GraphGUI(root)  # Create an instance of the app
            app.create_new_window()  # This will close the current window and open a new one
            root.mainloop()
        elif button_number == 8:
            app =TSPGUI(root)
            app.create_new_window()# Create an instance of the app  # This will close the current window and open a new one
            root.mainloop()
        elif button_number == 9:
            app =gui(root)
            app.create_new_window()# Create an instance of the app  # This will close the current window and open a new one
            root.mainloop()


        else:
            messagebox.showinfo("Button Clicked", f"You clicked '{self.get_button_name(button_number)}' Button")

    def get_button_name(self, button_number):
        button_names = [
            "Stack",
            "Single Linked List",
            "Doubly Linked List",
            "Queue",
            "Priority Queue",
            "Binary Tree",
            "Huffman Coding",
            "Graph",
            "Travelling Salesman Problem",
            "Hashtable",
        ]
        if 0 <= button_number < len(button_names):
            return button_names[button_number]
        return "Unknown"

    ### Doubly Linked List Functionality ###
    def run_doubly_linked_list_app(self):
        dll_window = tk.Toplevel(self.root)
        dll_window.title("Doubly Linked List Data Structure")
        dll_window.state("zoomed")
        dll_window.configure(bg='yellow')

        # Variables for the doubly linked list
        head = [None]
        size = [0]
        max_size = [None]

        # Create layout
        for i in range(6):
            dll_window.columnconfigure(i, weight=1)
        for i in range(4):
            dll_window.rowconfigure(i, weight=1)

        # Title
        title_label = tk.Label(dll_window, text="Doubly Linked List Data Structure", bg='yellow', font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, pady=10)

        # Entry for element
        input_label = tk.Label(dll_window, text="Enter Element:", bg='lightyellow', font=("Helvetica", 12))
        input_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        input_entry = tk.Entry(dll_window, font=("Helvetica", 12))
        input_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Set Max Size
        size_label = tk.Label(dll_window, text="Set Max Size:", bg='lightyellow', font=("Helvetica", 12))
        size_label.grid(row=1, column=2, padx=10, pady=10, sticky=tk.E)

        size_entry = tk.Entry(dll_window, font=("Helvetica", 12))
        size_entry.grid(row=1, column=3, padx=10, pady=10, sticky=tk.W)

        set_size_button = tk.Button(dll_window, text="Set Max Size", command=lambda: self.set_dll_max_size(size_entry, max_size), font=("Helvetica", 12))
        set_size_button.grid(row=1, column=4, padx=10, pady=10, sticky=tk.W)

        # Doubly Linked List operation buttons
        insert_begin_button = tk.Button(dll_window, text="Insert at Beginning", command=lambda: self.insert_dll_beginning_handler(input_entry, head, size, max_size, self.dll_canvas), font=("Helvetica", 12))
        insert_begin_button.grid(row=2, column=0, padx=10, pady=10)

        insert_end_button = tk.Button(dll_window, text="Insert at End", command=lambda: self.insert_dll_end_handler(input_entry, head, size, max_size, self.dll_canvas), font=("Helvetica", 12))
        insert_end_button.grid(row=2, column=1, padx=10, pady=10)

        delete_begin_button = tk.Button(dll_window, text="Delete at Beginning", command=lambda: self.delete_dll_beginning(head, size, self.dll_canvas), font=("Helvetica", 12))
        delete_begin_button.grid(row=2, column=2, padx=10, pady=10)

        delete_end_button = tk.Button(dll_window, text="Delete at End", command=lambda: self.delete_dll_end(head, size, self.dll_canvas), font=("Helvetica", 12))
        delete_end_button.grid(row=2, column=3, padx=10, pady=10)

        # Canvas to display doubly linked list
        self.dll_canvas = tk.Canvas(dll_window, bg='white')
        self.dll_canvas.grid(row=3, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

    def set_dll_max_size(self, size_entry, max_size):
        try:
            new_size = int(size_entry.get())
            if new_size <= 0:
                raise ValueError
            max_size[0] = new_size
            messagebox.showinfo("Success", f"Doubly Linked List max size set to {max_size[0]}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for linked list size")

    def insert_dll_beginning_handler(self, input_entry, head, size, max_size, canvas):
        value = input_entry.get().strip()
        if value:
            if max_size[0] is None or size[0] < max_size[0]:
                self.insert_dll_at_beginning(head, value)
                input_entry.delete(0, tk.END)
                size[0] += 1
                self.draw_dll(head, canvas)
            else:
                messagebox.showwarning("Warning", "Doubly Linked List has exceeded max size.")
        else:
            messagebox.showwarning("Warning", "Please enter a value")

    def insert_dll_end_handler(self, input_entry, head, size, max_size, canvas):
        value = input_entry.get().strip()
        if value:
            if max_size[0] is None or size[0] < max_size[0]:
                self.insert_dll_at_end(head, value)
                input_entry.delete(0, tk.END)
                size[0] += 1
                self.draw_dll(head, canvas)
            else:
                messagebox.showwarning("Warning", "Doubly Linked List has exceeded max size.")
        else:
            messagebox.showwarning("Warning", "Please enter a value")

    def delete_dll_beginning_handler(self, head, size, canvas):
        if head[0] is None:
            messagebox.showwarning("Warning", "Doubly Linked List is empty")
            return
        head[0] = head[0][2]  # Move head to the next node
        if head[0] is not None:
            head[0][1] = None  # Set previous of new head to None
        size[0] -= 1
        self.draw_dll(head, canvas)

    def delete_dll_end_handler(self, head, size, canvas):
        if head[0] is None:
            messagebox.showwarning("Warning", "Doubly Linked List is empty")
            return
        current = head[0]
        if current[2] is None:
            head[0] = None  # List becomes empty
        else:
            while current[2][2] is not None:
                current = current[2]
            current[2] = None  # Remove the last node
        size[0] -= 1
        self.draw_dll(head, canvas)

    def insert_dll_at_beginning(self, head, value):
        new_node = [value, None, head[0]]  # [value, prev, next]
        if head[0] is not None:
            head[0][1] = new_node  # Set the previous of the old head to the new node
        head[0] = new_node  # Move head to new node

    def insert_dll_at_end(self, head, value):
        new_node = [value, None, None]  # [value, prev, next]
        if head[0] is None:
            head[0] = new_node
            return
        current = head[0]
        while current[2] is not None:
            current = current[2]
        current[2] = new_node  # Link the last node to the new node
        new_node[1] = current  # Set the new node's previous to current

    def draw_dll(self, head, canvas):
        canvas.delete("all")
        current = head[0]
        x = 20
        while current is not None:
            # Draw rectangle for node
            canvas.create_rectangle(x, 50, x + 80, 100, fill="lightgreen")
            # Display node value
            canvas.create_text(x + 40, 75, text=current[0], font=("Helvetica", 12))
            # Draw previous arrow
            if current[1] is not None:
                canvas.create_line(x, 75, x - 20, 75, arrow=tk.LAST, fill="black")
            # Draw next arrow
            if current[2] is not None:
                canvas.create_line(x + 80, 75, x + 100, 75, arrow=tk.LAST, fill="black")
            x += 100
            current = current[2]

    ### Queue Functionality ###
    def run_queue_app(self):
        queue_window = tk.Toplevel(self.root)
        queue_window.title("Queue Data Structure")
        queue_window.state("zoomed")
        queue_window.configure(bg='#FFEB3B')  # Bright background for Queue

        # Configure grid
        for i in range(6):
            queue_window.columnconfigure(i, weight=1)
        for i in range(4):
            queue_window.rowconfigure(i, weight=1)

        # Title
        title_label = tk.Label(queue_window, text="Queue Data Structure", bg='#FFEB3B', font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, pady=10)

        # Entry for element
        input_label = tk.Label(queue_window, text="Enter Element:", bg='#FFEB3B', font=("Helvetica", 14))
        input_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        input_entry = tk.Entry(queue_window, font=("Helvetica", 14))
        input_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Set Queue size
        size_label = tk.Label(queue_window, text="Set Queue Size:", bg='#FFEB3B', font=("Helvetica", 14))
        size_label.grid(row=1, column=2, padx=10, pady=10, sticky=tk.E)

        size_entry = tk.Entry(queue_window, font=("Helvetica", 14))
        size_entry.grid(row=1, column=3, padx=10, pady=10, sticky=tk.W)

        set_size_button = tk.Button(queue_window, text="Set Size", command=lambda: self.set_queue_size(size_entry, queue_size), font=("Helvetica", 12))
        set_size_button.grid(row=1, column=4, padx=10, pady=10, sticky=tk.W)

        # Queue operation buttons
        enqueue_button = tk.Button(queue_window, text="Enqueue", command=lambda: self.enqueue(input_entry, queue, queue_size, canvas), font=("Helvetica", 12))
        enqueue_button.grid(row=2, column=0, padx=10, pady=10)

        dequeue_button = tk.Button(queue_window, text="Dequeue", command=lambda: self.dequeue(queue, canvas), font=("Helvetica", 12))
        dequeue_button.grid(row=2, column=1, padx=10, pady=10)

        peek_button = tk.Button(queue_window, text="Peek", command=lambda: self.peek_queue(queue), font=("Helvetica", 12))
        peek_button.grid(row=2, column=2, padx=10, pady=10)

        is_empty_button = tk.Button(queue_window, text="Is Empty", command=lambda: self.is_queue_empty(queue), font=("Helvetica", 12))
        is_empty_button.grid(row=2, column=3, padx=10, pady=10)

        # Canvas to display queue
        canvas = tk.Canvas(queue_window, bg='white')
        canvas.grid(row=3, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

        # Initialize queue variables
        queue = []
        queue_size = [5]  # Default size

    def set_queue_size(self, size_entry, queue_size):
        try:
            new_size = int(size_entry.get())
            if new_size <= 0:
                raise ValueError
            queue_size[0] = new_size
            messagebox.showinfo("Success", f"Queue size set to {queue_size[0]}")
            self.draw_queue(queue_size, queue_size, canvas=self.root)  # Redraw if necessary
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for queue size")

    def enqueue(self, input_entry, queue, queue_size, canvas):
        item = input_entry.get().strip()
        if item:
            if len(queue) < queue_size[0]:
                queue.append(item)
                input_entry.delete(0, tk.END)
                self.draw_queue(queue, canvas)
            else:
                messagebox.showwarning("Warning", "Queue Overflow")
        else:
            messagebox.showwarning("Warning", "Please enter an element to enqueue")

    def dequeue(self, queue, canvas):
        if queue:
            item = queue.pop(0)
            messagebox.showinfo("Dequeue", f"Dequeued Element: {item}")
            self.draw_queue(queue, canvas)
        else:
            messagebox.showwarning("Warning", "Queue Underflow")

    def peek_queue(self, queue):
        if queue:
            front_item = queue[0]
            messagebox.showinfo("Peek", f"Front Element: {front_item}")
        else:
            messagebox.showwarning("Warning", "Queue is empty")

    def is_queue_empty(self, queue):
        if not queue:
            messagebox.showinfo("Queue Status", "Queue is empty")
        else:
            messagebox.showinfo("Queue Status", "Queue is not empty")

    def draw_queue(self, queue, canvas):
        canvas.delete("all")
        x_start = 20
        y_start = 100
        box_width = 80
        box_height = 50
        padding = 20
        for idx, item in enumerate(queue):
            x = x_start + idx * (box_width + padding)
            canvas.create_rectangle(x, y_start, x + box_width, y_start + box_height, fill="lightblue")
            canvas.create_text(x + box_width / 2, y_start + box_height / 2, text=item, font=("Helvetica", 12))
            # Draw arrow to next element if not the last
            if idx < len(queue) - 1:
                canvas.create_line(x + box_width, y_start + box_height / 2, x + box_width + padding, y_start + box_height / 2, arrow=tk.LAST)

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.size

    def set_size(self, size):
        self.size = size

    def enqueue(self, process, priority):
        if self.is_full():
            raise OverflowError("Priority Queue is full")
        else:
            self.queue.append((process, priority))
            self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)[0]
        else:
            raise IndexError("dequeue from empty priority queue")

    def traverse(self):
        if self.is_empty():
            return []
        else:
            return self.queue



if __name__ == "__main__":
   root = tk.Tk()
   app = ButtonApp(root)
   root.mainloop()
