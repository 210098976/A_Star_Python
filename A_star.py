# -----------
# From Sebastian Thrun Udacity online classes
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = ((9, 8, 7, 6, 5, 4),
             (8, 7, 6, 5, 4, 3),
             (7, 6, 5, 4, 3, 2),
             (6, 5, 4, 3, 2, 1),
             (5, 4, 3, 2, 1, 0))

init = (0, 0)
goal = (len(grid[0])-1, len(grid)-1)

# cost must not be 0 because now it affects more than p_queue sorting
cost = 1

delta = ((0, -1), # go up
         (-1, 0), # go left
         (0, 1), # go down
         (1, 0)) # go right

def get_neighbors(x, y):
    return tuple(map(lambda i: (x+i[0], y+i[1]), delta))

def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    prev = [[[] for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[y][x]

    p_queue = [(f, g, x, y)]
    path = []
    log = []

    while p_queue:
        p_queue.sort()
        f, g, x, y = p_queue.pop(0)
        grid[y][x] = 1 # closed

        if x == goal[0] and y == goal[1]:
            path = [(x, y)]
            break

        neighbors = get_neighbors(x, y)

        for i in neighbors:
            xi, yi = i

            if yi < 0 or yi >= len(grid) or xi < 0 or xi >= len(grid[0]):
                continue

            gi = g + cost

            f = gi + heuristic[yi][xi] # a star
            # f = heuristic[yi][xi] # best first?
            # f = gi # ucs

            if not grid[yi][xi]:
                p_queue.append((f, gi, xi, yi))

            p = prev[yi][xi]

            if (not p or gi < p[1]):
            # if (not p or gi <= p[1]):
                if (p and p[0] != (x, y)):
                    log.append("({}, {}): {} => {}".format(xi, yi, p, np))
                np = [(x, y), gi]
                p[:] = np


    if not path:
        print("Fail")
        return path

    if log:
        for i in log:
            print(i)
        print()

    while path[-1] != (0, 0):
        x, y = path[-1]
        p = prev[y][x][0]
        if p in path:
            print("Loop! {} in in {}".format(p, path))
            return []
        path.append(p)

    while path:
        x, y = path.pop(0)
        expand[y][x] = len(path)

    return expand

result = search(grid, init, goal, cost, heuristic)

for el in result:
    print("  ".join([*map(lambda x: "%2s" %x, el)]))
