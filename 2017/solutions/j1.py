def quadrant_selection(x, y):
    if (x > 0): # x+
        if (y > 0): # y+
            return 1
        return 4 # y-
    # x-
    if (y > 0):
        return 2 # y+
    return 3 # y-

x = int(input())
y = int(input())
print(quadrant_selection(x, y))