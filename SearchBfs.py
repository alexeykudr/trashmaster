class BreadthSearchAlgorithm:
    def __init__(self, graph, start, target):
        self.graph = graph
        self.start = start
        self.target = target

    def bfs(self):
        queue = [[self.start]]
        visited = []

        if self.start == self.target:
            return

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = self.graph
                for neighbour in neighbours:
                    next_path = list(path)
                    next_path.append(neighbour)
                    queue.append(next_path)
                    if neighbour == self.target:
                        return next_path
                visited.append(node)

        return "Path found"
