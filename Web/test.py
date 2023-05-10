import tkinter as tk

root = tk.Tk()
root.title("My GUI")

label = tk.Label(root, text="Hello World!")
label.pack()

button = tk.Button(root, text="Click me!", command=lambda: label.config(text="Button clicked!"))
button.pack()

root.mainloop()