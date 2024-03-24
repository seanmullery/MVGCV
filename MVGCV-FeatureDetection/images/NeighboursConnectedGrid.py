import matplotlib.pyplot as plt

# Function to set up the axes properties
def setup_ax(ax):
    ax.set_facecolor('white')  # Set the background color to white
    ax.axis('off')             # Remove the axes
    ax.set_aspect('equal')     # Set the aspect ratio to be equal
    ax.set_xlim(0, 3)          # Set x limits to match the grid size
    ax.set_ylim(0, 3)          # Set y limits to match the grid size

# Function to draw and shade the Sudoku grid
def draw_shade_sudoku_grid(ax, shade_extra_squares=None):
    # Draw the Sudoku grid lines
    for x in range(4):
        ax.plot([x, x], [0, 3], color='black', lw=2)
        ax.plot([0, 3], [x, x], color='black', lw=2)

    # Shade the middle square red
    ax.fill_between([1, 2], [1, 1], [2, 2], color='red', alpha=0.5)

    # Shade the specified squares green
    ax.fill_between([1, 2], [2, 2], [3, 3], color='green', alpha=0.5)  # Middle upper square
    ax.fill_between([1, 2], [0, 0], [1, 1], color='green', alpha=0.5)  # Middle lower square
    ax.fill_between([0, 1], [1, 1], [2, 2], color='green', alpha=0.5)  # Middle left square
    ax.fill_between([2, 3], [1, 1], [2, 2], color='green', alpha=0.5)  # Middle right square

    # Shade additional squares if specified
    if shade_extra_squares:
        for square in shade_extra_squares:
            ax.fill_between([square[0], square[1]], [square[2], square[2]], [square[3], square[3]], color='green', alpha=0.5)

# Create a figure to accommodate three grids side by side with reduced space in between
fig = plt.figure(figsize=(18, 5))

# Create subplots for each Sudoku grid
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Set up all subplots
setup_ax(ax1)
setup_ax(ax2)
setup_ax(ax3)

# Draw and shade the left Sudoku grid (without additional squares)
draw_shade_sudoku_grid(ax1)

# Draw and shade the middle Sudoku grid (with additional squares for "Six Connected")
draw_shade_sudoku_grid(ax2, shade_extra_squares=[(0, 1, 2, 3), (2, 3, 0, 1)])

# Draw and shade the right Sudoku grid (with corner squares shaded for "Eight Connected")
draw_shade_sudoku_grid(ax3, shade_extra_squares=[(0, 1, 2, 3), (2, 3, 2, 3), (0, 1, 0, 1), (2, 3, 0, 1)])

# Add titles above each Sudoku grid
ax1.set_title("Four Connected", fontsize=16)
ax2.set_title("Six Connected", fontsize=16)
ax3.set_title("Eight Connected", fontsize=16)

# Adjust the subplots to provide less space between them
fig.subplots_adjust(wspace=0.15)
plt.savefig("ConnectedNeighbours.jpg")

# Show the plot
plt.show()

