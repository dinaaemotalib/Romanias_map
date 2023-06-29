import tkinter as tk
import queue

# button function that show result


def submit():

    # get input
    start_city = intial.get()
    end_city = goal.get()

# call function
    bfs_path = bfs(start_city, end_city)
    astar_path = astar(start_city, end_city)
    uniform_cost_path = uniform_cost(start_city, end_city)
    dfs_path = dfs(start_city, end_city)

# printing in terminal
    print("BFS path:", bfs_path)
    print("A* path:", astar_path)
    print("Uniform Cost path:", uniform_cost_path)
    print("DFS path:", dfs_path)


    # Define the graph
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


# Breadth-First Search (BFS)
def bfs(start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        if node == end:
            return path
        for next_node in graph[node]:
            if next_node not in path:
                queue.append((next_node, path + [next_node]))


# A* Search
def heuristic(node, end):
    # it assumes all distances are equal
    return 0


def astar(start, end):
    open_set = queue.PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    while not open_set.empty():
        _, current = open_set.get()
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))
        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, end)
                open_set.put((f_score, neighbor))


# Uniform Cost Search
def uniform_cost(start, end):
    open_set = queue.PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    while not open_set.empty():
        _, current = open_set.get()
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))
        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                open_set.put((tentative_g_score, neighbor))


# Depth-First Search (DFS)
def dfs(start, end):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        if node == end:
            return path
        for next_node in graph[node]:
            if next_node not in path:
                stack.append((next_node, path + [next_node]))


# Create a Tkinter window
window = tk.Tk()
window.geometry("500x200")

# Create a Text widget
text_widget = tk.Text(window, height=1, width=12)
text_widget.place(x=55, y=20)
text_widget.insert(tk.END, "intial state")

# input box
intial = tk.Entry(window, width=30)
intial.place(x=200, y=20)

# Create a Text widget
text_widget1 = tk.Text(window, height=1, width=12)
text_widget1.place(x=55, y=50)
text_widget1.insert(tk.END, "goal state")

# input box
goal = tk.Entry(window, width=30)
goal.place(x=200, y=50)

# button
button = tk.Button(window, text="Submit", command=submit)
button.place(x=260, y=70)

# loop to stay open utill i trun it off
window.mainloop()
