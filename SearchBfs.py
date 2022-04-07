class BreadthSearchAlgorithm:
    def __init__(self, start, target):
        self.graph = self.getData()
        self.start = start
        self.target = target

    def bfs(self):
        print("It's showtime")
        can_go = [self.start]
        visited = []
        if self.start == self.target:
            print("Start = Target")
            return -1
        while can_go != []:
            node = can_go.pop(0)
            if node not in visited:
                visited.append(node)
                if node == self.target:
                    return visited
                neighbours = self.graph.get(node, [])
                for neighbour in neighbours:
                    can_go.append(neighbour)
            print(visited)
        return -1

    def getData(self):
        with open("data.txt", "r") as f:
            matrix = [
                [int(x) for x in line.split(",") if x != "\n"] for line in f.readlines()
            ]
        adj = {}
        for yi, yvalue in enumerate(matrix):
            for xi, xvalue in enumerate(matrix):
                if xi - 1 >= 0 and matrix[yi][xi - 1] == 0:
                    adj[(xi, yi)] = adj.get((xi, yi), []) + [(xi - 1, yi)]

                if xi + 1 < len(matrix[yi]) and matrix[yi][xi + 1] == 0:
                    adj[(xi, yi)] = adj.get((xi, yi), []) + [(xi + 1, yi)]

                if yi - 1 >= 0 and matrix[yi - 1][xi] == 0:
                    adj[(xi, yi)] = adj.get((xi, yi), []) + [(xi, yi - 1)]

                if yi + 1 < len(matrix) and matrix[yi + 1][xi] == 0:
                    adj[(xi, yi)] = adj.get((xi, yi), []) + [(xi, yi + 1)]

        return adj