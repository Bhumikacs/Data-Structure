from tkinter import *
from tkinter import messagebox

class StackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Data Structure")
        self.root.state("zoomed")
        self.root['bg'] = '#5C6BC0'

        # Configuring row and column
        self.root.columnconfigure((0, 1, 2, 3, 4, 5), weight=10)
        self.root.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Stack size input
        size_label = Label(self.root, text="Enter stack size:")
        size_label.grid(row=0, column=0, ipadx=6, ipady=6, padx=10, sticky=E)

        self.size_entry = Entry(self.root)
        self.size_entry.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, sticky=W)

        # Stack operations input
        input_label = Label(self.root, text="Enter the number:")
        input_label.grid(row=1, column=0, ipadx=7, ipady=7, padx=10, sticky=E)

        self.input_entry = Entry(self.root)
        self.input_entry.grid(row=1, column=1, ipadx=5, ipady=5, padx=5, sticky=W)

        # Stack operation buttons
        push_button = Button(self.root, text="Push", command=self.push)
        push_button.grid(row=1, column=2, ipadx=5, ipady=5, padx=5, sticky=W)

        pop_button = Button(self.root, text="Pop", command=self.pop)
        pop_button.grid(row=1, column=3, ipadx=5, ipady=5, padx=5, sticky=W)

        peek_button = Button(self.root, text="Peek", command=self.peek)
        peek_button.grid(row=1, column=4, ipadx=5, ipady=5, padx=5, sticky=W)

        is_empty_button = Button(self.root, text="Is Empty", command=self.is_empty)
        is_empty_button.grid(row=1, column=5, ipadx=5, ipady=5, padx=5, sticky=W)

        self.canvas = Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

        # Initialize stack-related attributes
        self.stack = []
        self.stack_top = 0
        self.stack_size = 5  # Default stack size
        self.item_height = 40

        # Add a button to set the stack size
        set_size_button = Button(self.root, text="Set Stack Size", command=self.set_stack_size)
        set_size_button.grid(row=0, column=2, ipadx=5, ipady=5, padx=5, sticky=W)

    def draw_stack(self):
        self.canvas.delete("all")
        y = 400
        for item in self.stack:
            self.canvas.create_rectangle(200, y - self.item_height, 400, y, fill="lightblue")
            self.canvas.create_text(300, y - self.item_height // 2, text=item, font=("Helvetica", 16))
            y -= self.item_height

    def set_stack_size(self):
        try:
            self.stack_size = int(self.size_entry.get())
            if self.stack_size <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for stack size")

    def push(self):
        if self.stack_top < self.stack_size:
            item = self.input_entry.get()
            if item:
                self.stack.append(item)
                self.input_entry.delete(0, END)
                self.draw_stack()
                self.stack_top += 1
            else:
                messagebox.showwarning("Warning", "Please enter a number")
        else:
            messagebox.showwarning("Warning", "Stack Overflow")

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.draw_stack()
            self.stack_top -= 1
        else:
            messagebox.showwarning("Warning", "Stack Underflow")

    def peek(self):
        if self.stack:
            top_item = self.stack[-1]
            messagebox.showinfo("Peek", f"Top item: {top_item}")
        else:
            messagebox.showwarning("Warning", "Stack is empty")

    def is_empty(self):
        if self.stack:
            messagebox.showinfo("Is Empty", "Stack is not empty")
        else:
            messagebox.showinfo("Is Empty", "Stack is empty")
    def create_new_window(self):
        self.destroy_window()  # Close the current window
        new_root = Tk()
        new_app = StackGUI(new_root)  # Create a new instance of the app
        new_root.attributes('-topmost', True)  # Bring new window to the front
        new_root.mainloop()

    def destroy_window(self):
        self.root.destroy()  # Close the current window
if __name__ == "__main__":
    root = Tk()
    app = StackGUI(root)
    root.mainloop()
