import heapq
from collections import Counter
import tkinter as tk
from tkinter import messagebox,simpledialog
from tkinter import Label,Entry,Button
from priority_queue import PriorityQueueApp
from binary_tree import BinaryTreeGUI
from tkinter import *
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def generate_code(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_code(node.left, prefix + "0", codebook)
        generate_code(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_code(root)
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            current_code = ""
    return decoded_data

class HuffmanCodingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding GUI")
        self.root.state("zoomed")
        self.root.configure(bg="#66CCCC")

        # Title
        self.title_label = Label(root, text="Huffman Coding", font=("Times New Roman", 24), bg="#66CCCC")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.rollno_label = Label(root, text="S113", font=("Times New Roman", 18), bg="#66CCCC")
        self.rollno_label.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Input for Encoding
        self.input_label = Label(root, text="Enter Data:", font=("Arial", 16), bg="#66CCCC")
        self.input_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.input_entry = Entry(root, font=("Arial", 16), width=50)
        self.input_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Encode Button
        self.encode_button = Button(root, text="Encode", font=("Arial", 16), command=self.encode_data)
        self.encode_button.grid(row=2, column=2, padx=20, pady=10, sticky="w")

        # Clear Button
        self.clear_button = Button(root, text="Clear", font=("Arial", 16), command=self.clear_encoding)
        self.clear_button.grid(row=2, column=3, padx=20, pady=10, sticky="w")

        # Result of Encoding
        self.encoded_label = Label(root, text="Encoded Data:", font=("Arial", 16), bg="#66CCCC")
        self.encoded_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.encoded_result = Label(root, text="", font=("Arial", 16), bg="white", width=50)
        self.encoded_result.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # Codebook
        self.codebook_label = Label(root, text="Codebook:", font=("Arial", 16), bg="#66CCCC")
        self.codebook_label.grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.codebook_result = Label(root, text="", font=("Arial", 16), bg="white", width=50, wraplength=600, justify=LEFT)
        self.codebook_result.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # Input for Decoding
        self.decode_label = Label(root, text="Enter Encoded Data:", font=("Arial", 16), bg="#66CCCC")
        self.decode_label.grid(row=5, column=0, padx=20, pady=10, sticky="e")
        self.decode_entry = Entry(root, font=("Arial", 16), width=50)
        self.decode_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        # Decode Button
        self.decode_button = Button(root, text="Decode", font=("Arial", 16), command=self.decode_data)
        self.decode_button.grid(row=5, column=2, padx=20, pady=10, sticky="w")

        # Clear Decoding Button
        self.clear_decoding_button = Button(root, text="Clear", font=("Arial", 16), command=self.clear_decoding)
        self.clear_decoding_button.grid(row=5, column=3, padx=20, pady=10, sticky="w")

        # Result of Decoding
        self.decoded_label = Label(root, text="Decoded Data:", font=("Arial", 16), bg="#66CCCC")
        self.decoded_label.grid(row=6, column=0, padx=20, pady=10, sticky="e")
        self.decoded_result = Label(root, text="", font=("Arial", 16), bg="white", width=50)
        self.decoded_result.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        # Codebook for Decoding
        self.codebook_input_label = Label(root, text="Codebook Entries:", font=("Arial", 16), bg="#66CCCC")
        self.codebook_input_label.grid(row=7, column=0, columnspan=3, padx=20, pady=20)

        # Codebook Entries Frame
        self.codebook_frame = Frame(root, bg="#66CCCC")
        self.codebook_frame.grid(row=8, column=0, columnspan=3, padx=20, pady=10)
        self.codebook_entries = []
        self.add_codebook_entry()

    def add_codebook_entry(self):
        entry_frame = Frame(self.codebook_frame, bg="#66CCCC")
        entry_frame.pack(anchor="w", pady=5)
        char_entry = Entry(entry_frame, font=("Arial", 14), width=5)
        char_entry.pack(side=LEFT, padx=5)
        binary_entry = Entry(entry_frame, font=("Arial", 14), width=20)
        binary_entry.pack(side=LEFT, padx=5)
        self.codebook_entries.append((char_entry, binary_entry))

        add_button = Button(entry_frame, text="Add", font=("Arial", 14), command=self.add_codebook_entry)
        add_button.pack(side=LEFT, padx=10)

    def encode_data(self):
        data = self.input_entry.get().strip()
        if data:
            encoded_data, codebook = huffman_encoding(data)
            self.encoded_result.config(text=encoded_data)
            formatted_codebook = ", ".join(f"{char}: {code}" for char, code in codebook.items())
            self.codebook_result.config(text=formatted_codebook)
        else:
            messagebox.showwarning("Warning", "Input data cannot be empty")

    def decode_data(self):
        encoded_data = self.decode_entry.get().strip()
        codebook = {}
        for char_entry, binary_entry in self.codebook_entries:
            char = char_entry.get().strip()
            binary = binary_entry.get().strip()
            if char and binary:
                codebook[char] = binary  # Store the character as the key and binary code as the value

        if encoded_data and codebook:
            decoded_data = huffman_decoding(encoded_data, codebook)
            self.decoded_result.config(text=decoded_data)
        else:
            messagebox.showwarning("Warning", "Encoded data and codebook cannot be empty")

    def clear_encoding(self):
        self.input_entry.delete(0, END)
        self.encoded_result.config(text="")
        self.codebook_result.config(text="")
    def clear_decoding(self):
        self.decode_entry.delete(0, END)
        self.decoded_result.config(text="")
        for char_entry, binary_entry in self.codebook_entries:
            char_entry.delete(0, END)
            binary_entry.delete(0, END)
    def create_new_window(self):
        self.destroy_window()  # Close the current window
        new_root = tk.Tk()
        new_app = HuffmanCodingApp(new_root)  # Create a new instance of the app
        new_root.attributes('-topmost', True)  # Bring new window to the front
        new_root.mainloop()

    def destroy_window(self):
        self.root.destroy()  # Close the current windo

if __name__ == "__main__":
    root = Tk()
    app = HuffmanCodingApp(root)
    root.mainloop()
