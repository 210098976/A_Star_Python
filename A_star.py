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

    queue = { (x, y): (f, g) }
    p_queue = queue.keys()
    count = []

    while p_queue:
        p_queue = sorted(queue.keys(), key=lambda x: queue[x][0])
        k = p_queue[0]
        x, y = k
        f, g = queue[k]
        del queue[k]

        grid[y][x] = 1 # close

        neighbors = get_neighbors(x, y)

        # rebase
        while count and count[0] not in neighbors:
            xp, yp = count.pop(0)
            expand[yp][xp] = -1

        # if ever rebased, it *might* no longer be guaranteed that
        # nodes in p_queue must at least have a neighbor in count
        if not count and (x, y) != (0, 0):
            print("Fail")
            return []

        print((x, y), len(count))
        expand[y][x] = len(count)
        count.insert(0, (x, y))

        if x == goal[0] and y == goal[1]:
            return expand

        for i in neighbors:
            xi, yi = i
            gi = g + cost

            if yi < 0 or yi >= len(grid) or xi < 0 or xi >= len(grid[0]):
                continue

            f = gi + heuristic[yi][xi]

            if not grid[yi][xi]:
                if ((xi, yi) in queue):
                    c = queue[(xi, yi)]
                    if c != (f, gi):
                        print("{}: {} => {}".format((xi, yi), c, (f, gi)))
                    else:
                        print("{}: {}".format((xi, yi), c))
                queue[(xi, yi)] = (f, gi)
                # grid[yi][xi] = 1

    print("Fail")
    return []

result = search(grid, init, goal, cost, heuristic)

for el in result:
    print("  ".join([*map(lambda x: "%2s" %x, el)]))
