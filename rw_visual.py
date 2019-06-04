import matplotlib.pyplot as plt

from random_walk import RandomWalk


def paint_spatter(x_vals, y_vals):
    colors = []
    for i in range (0, len(x_vals)):

        hex_strawberry = '#f82a2a'
        hex_light_green = '#8ef82a'
        hex_blue = '#2e2af8'
        hex_yellow = '#f8e72a'

        """choose a color based on the position of point
        comparing to the previous point """
        
        if(y_vals[i] < y_vals[i-1]):
            colors.append(hex_strawberry)
        elif(y_vals[i] > y_vals[i-1]):
            colors.append(hex_light_green)
        elif(x_vals[i] < x_vals[i-1]):
            colors.append(hex_blue)
        elif(x_vals[i] > x_vals[i-1]):
            colors.append(hex_yellow)

    return colors
    
# Keep making new walks, as long as the program is active.
while True:
    num_of_dots = 50000
    # Make a random walk, and plot the points.
    rw = RandomWalk(num_of_dots)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))

    """ deleted colorMap parameter and changed color parameter """
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.ocean, edgecolor='none', s=1)
        
    # Emphasize the first and last points.
    #plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    #plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
        
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
        
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
