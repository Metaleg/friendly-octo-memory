from graphviz import Digraph
from queue import Queue
from queue import PriorityQueue


def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(a.x - b.x) + abs(a.y - b.y)


def print_graph(graph, name):
    dot = Digraph(comment=str(name))

    for i in range(len(graph)):
        for key, value in graph[i].items():
            dot.edge(str(i), str(key), constraint='true', label=str(value))

    print(dot.source)
    dot.render(str(name), view=True)


def print_path_no_weights(path, name):
    dot = Digraph(comment=str(name))

    for i in range(len(path)):
        if i != len(path) - 1:
            dot.edge(str(path[i]), str(path[i + 1]))

    print(dot.source)
    dot.render(str(name), view=True)


def bfs(input_graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in input_graph[int(current)]:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    current = goal
    path = [current]
    while current != start:
        current = came_from[str(current)]
        path.append(current)
    path.reverse()

    name = 'bfs'
    print_path_no_weights(path, name)


def dijkstra(input_graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in input_graph[int(current)]:
            new_cost = cost_so_far[current] + input_graph[int(current)][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    current = goal
    path = [current]
    while current != start:
        current = came_from[str(current)]
        path.append(current)
    path.reverse()

    name = 'dijkstra'
    print_path_no_weights(path, name)


# def dfs(input_graph, start, goal):
#     frontier = Queue()
#     frontier.put(start)
#     came_from = {start: None}
#
#     while not frontier.empty():
#         current = frontier.get()
#         if current == goal:
#             break
#         for next in input_graph[int(current)]:

# def a_star(input_graph, start, goal):
#     frontier = PriorityQueue()
#     frontier.put(start, 0)
#     came_from = {start: None}
#
#     while not frontier.empty():
#         current = frontier.get()
#         if current == goal:
#             break
#         for next in input_graph[int(current)]:
#             if next not in came_from:
#                 priority = heuristic(goal, next)
#                 frontier.put(next, priority)
#                 came_from[next] = current
#
#     current = goal
#     path = [current]
#     while current != start:
#         current = came_from[str(current)]
#         path.append(current)
#     path.reverse()
#
#     name = 'a_star'
#     print_path_no_weights(path, name)


input_graph = [
    {'1': 2, '2': 1, '3': 3, '4': 9, '5': 40},
    {'2': 4, '4': 3},
    {'3': 8},
    {'4': 7},
    {'5': 5},
    {'2': 2, '6': 2, '7': 2},
    {'5': 1, '7': 6},
    {'5': 9, '6': 8}
]

name = 'source'
print_graph(input_graph, name)

bfs(input_graph, 0, 6)
dijkstra(input_graph, 0, 6)
# a_star(input_graph, 0, 6)

