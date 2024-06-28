def initialize_visited(rows, cols):
    return [[False for _ in range(cols)] for _ in range(rows)]

def dfs_recursive(maze, visited, path, i, j, goal):
    rows, cols = len(maze), len(maze[0])
    
    if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or maze[i][j] == 1:
        return False
    
    path.append((i, j))
    visited[i][j] = True
    
    if (i, j) == goal:
        return True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if dfs_recursive(maze, visited, path, ni, nj, goal):
            return True
    
    path.pop()
    return False

def find_path_dfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = initialize_visited(rows, cols)
    path = []
    
    dfs_recursive(maze, visited, path, start[0], start[1], goal)
    return path

# Ejemplo de uso
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Nodo inicial
goal = (4, 4)   # Nodo objetivo

path = find_path_dfs(maze, start, goal)
print(path)
