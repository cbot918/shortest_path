from collections import defaultdict

# 定義一個類來表示圖
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # 添加邊到圖
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    # 窮舉法查找所有路徑
    def find_all_paths(self, start, end, path=[], weight=0):
        path = path + [(start, weight)]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node, node_weight in self.graph[start]:
            if node not in [p[0] for p in path]:
                newpaths = self.find_all_paths(node, end, path, node_weight)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    # 尋找最短路徑
    def find_shortest_path(self, start, end):
        paths = self.find_all_paths(start, end)
        shortest_path = min(paths, key=lambda x: sum([p[1] for p in x]))
        return shortest_path

# 創建圖並添加邊


# 尋找最短路徑
start = 'B'
end = 'D'
shortest_path = g.find_shortest_path(start, end)

print("最短路徑:", shortest_path)
