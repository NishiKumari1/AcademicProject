# import all the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random

# set the style of the graph
plt.style.use('fivethirtyeight')

# input the size of the array (list here)
# and shuffle the elements to create
# a random list
n = int(input("enter array size\n"))
a = [i for i in range(1, n + 1)]
random.shuffle(a)


# insertion sort

s=input("enter sorting name:")

if(s=="insertion"):

    def s(a):
        n = len(a)

        # Traverse through 1 to n
        for i in range(1, n):
            key = a[i]
            j = i - 1

            # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            while j >= 0 and key < a[j]:
                a[j + 1] = a[j]
                j -= 1
                yield a
            a[j + 1] = key
            yield a


# selection sort

elif(s=="selection"):

    def s(a):
        n = len(a)
        for i in range(n):

            # Find the minimum element in the unsorted portion of the array
            min_idx = i
            for j in range(i + 1, n):
                if a[j] < a[min_idx]:
                    min_idx = j

            # Swap the minimum element with the first element of the unsorted portion
            a[i], a[min_idx] = a[min_idx], a[i]
            yield a

# Bubble sort

elif (s == "bubble"):

    def s(a):
        n = len(a)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already sorted
            for j in range(0, n - i - 1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    yield a



# generator object returned by the function
generator = s(a)

# to set the colors of the bars.
data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
    "my_map",
    {
        "red": [(0, 1.0, 1.0),
                (1.0, .5, .5)],
        "green": [(0, 0.5, 0.5),
                  (1.0, 0, 0)],
        "blue": [(0, 0.50, 0.5),
                 (1.0, 0, 0)]
    }
)

fig, ax = plt.subplots()

# the bar container
rects = ax.bar(range(len(a)), a, align="edge",
               color=color_map(data_normalizer(range(n))))

# setting the view limit of x and y axes
ax.set_xlim(0, len(a))
ax.set_ylim(0, int(1.1 * len(a)))

# the text to be shown on the upper left
# indicating the number of iterations
# transform indicates the position with
# relevance to the axes coordinates.
text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]


# function to be called repeatedly to animate


def animate(A, rects, iteration):
    # setting the size of each bar equal
    # to the value of the elements
    for rect, val in zip(rects, A):
        rect.set_height(val)

    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0]))


anim = FuncAnimation(fig, func=animate,
                     fargs=(rects, iteration), frames=generator, interval=50,
                     repeat=False)

plt.show()