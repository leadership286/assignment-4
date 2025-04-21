import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(event, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse coordinates
    mouse_x, mouse_y = event.x, event.y
    
    # Calculate the position of the eraser
    left_x = mouse_x - ERASER_SIZE // 2
    top_y = mouse_y - ERASER_SIZE // 2
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Iterate through all the cells on the canvas and check if they overlap with the eraser
    for item in canvas.find_overlapping(left_x, top_y, right_x, bottom_y):
        canvas.itemconfig(item, fill="white")

def create_grid():
    """Create a grid of blue cells on the canvas."""
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            # Draw the cell
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue", outline="blue")

# Initialize tkinter window
root = tk.Tk()
root.title("Canvas Eraser Tool")

# Create canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Create the grid on the canvas
create_grid()

# Create the eraser, initially positioned at the top-left corner of the window
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="pink")

# Bind mouse motion to move the eraser and erase
canvas.bind("<B1-Motion>", lambda event: erase_objects(event, eraser))

# Run the tkinter main loop
root.mainloop()
