#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_fibonacci_squares(n):
    # Generate Fibonacci sequence
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])

    fig, ax = plt.subplots()
    x, y = 0, 0
    angle = 0
    cx,cy = x+fib[1],y+fib[1]   #coordinates for center of the circle, bc of middle in diferent corners

    for i in range(1, n):
        square = patches.Rectangle((x, y), fib[i], fib[i], fill=None, edgecolor='b')
        ax.add_patch(square)

        # Draw quarter circle inside the square
        circle = patches.Arc((cx, cy), 2*fib[i], 2*fib[i], angle=angle, theta1=180, theta2=270, edgecolor='r')
        ax.add_patch(circle)
        # Add number of Fibonnaci sequence in the middle of the square
        ax.text(x+fib[i]/2, y+fib[i]/2, str(fib[i]), color='black', 
        ha='center', va='center', fontsize=8)

        # First 2 squares are special cases
        if i == 1:
            x += fib[i]
        elif i == 2:
            x -= fib[i]
            y += fib[i]
            cx,cy = x,y 
        # Update position for the next square
        else:
            if angle == 0:
                x += fib[i]
                y += 0
                cx,cy = x,y+fib[i]+fib[i-1]
            elif angle == 90:
                x -= fib[i-1]
                y += fib[i]
                cx,cy = x,y 
            elif angle == 180:
                x -= fib[i]+fib[i-1]
                y -= fib[i-1]
                cx,cy = x+fib[i]+fib[i-1],y
            elif angle == 270:
                x += 0
                y -= fib[i]+fib[i-1]
                cx,cy = x+fib[i]+fib[i-1],y+fib[i]+fib[i-1]

        angle = (angle + 90) % 360

    # Set the aspect of the plot to be equal
    ax.set_aspect('equal')
    plt.xlim(-fib[-1]*1.5, fib[-1])
    plt.ylim(-fib[-1]*1.25, fib[-1]*1.25)
    plt.grid(True)
    plt.show()

# Example usage
plot_fibonacci_squares(21)