import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Flappy Bird")

# Set up the canvas
canvas = tk.Canvas(window, width=400, height=600)
canvas.pack()

# Create the bird
bird = canvas.create_oval(50, 300, 100, 350, fill="yellow")

# Function to make the bird jump
def jump(event):
    canvas.move(bird, 0, -50)

# Bind the spacebar key to the jump function
window.bind("<space>", jump)

# Function to move the pipes
def move_pipes():
    canvas.move(pipes, -5, 0)
    window.after(50, move_pipes)

# Create the pipes
pipes = canvas.create_rectangle(400, 0, 450, 200, fill="green")

# Start moving the pipes
move_pipes()

# Start the main loop
window.mainloop()