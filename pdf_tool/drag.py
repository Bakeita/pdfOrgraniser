import tkinter as tk

class DraggableLabel(tk.Label):
    def __init__(self, master, text, **kwargs):
        tk.Label.__init__(self, master, text=text, **kwargs)
        self.bind("<Button-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        x = self.winfo_x() + (event.x - self.start_x)
        y = self.winfo_y() + (event.y - self.start_y)
        self.place(x=x, y=y)

class SwapApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Drag to Swap Example")

        self.label1 = DraggableLabel(self, text="Label 1", relief=tk.RAISED, borderwidth=2)
        self.label1.place(x=50, y=50)

        self.label2 = DraggableLabel(self, text="Label 2", relief=tk.RAISED, borderwidth=2)
        self.label2.place(x=200, y=50)

    def swap_positions(self):
        x1, y1 = self.label1.winfo_x(), self.label1.winfo_y()
        x2, y2 = self.label2.winfo_x(), self.label2.winfo_y()

        self.label1.place(x=x2, y=y2)
        self.label2.place(x=x1, y=y1)

if __name__ == "__main__":
    app = SwapApp()

    swap_button = tk.Button(app, text="Swap", command=app.swap_positions)
    swap_button.place(x=150, y=150)

    app.mainloop()
