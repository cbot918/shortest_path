import heapq

class Edge:
  def __init__(self, v1, v2, w):
    self.weight = w
    self.start_vertex = v1
    self.target_vertex = v2

class Node:
  def __init__(self,v1):
    self.name = v1
    self.neighbors = []
    self.min_distance = float('Inf')
    self.visited = False
    self.predecessor = None

  def __lt__(self, other):
    return self.min_distance < other.min_distance

  def add_edge(self, w, v2):
    new_edge = Edge(self, v2, w)
    self.neighbors.append(new_edge)

class Dijkstra:
  def __init__(self, start=None):
    self.heap = []
    # self.start = start

  def calculate(self, start):
    self.start = start
    start.min_distance = 0
    heapq.heappush(self.heap, start)
    while self.heap:
      current_vertex = heapq.heappop(self.heap)
      if current_vertex.visited:
        continue
      for edge in current_vertex.neighbors:
        start_vertex = edge.start_vertex
        target_vertex = edge.target_vertex
        new_distance = current_vertex.min_distance+edge.weight
        if new_distance < target_vertex.min_distance:
          target_vertex.min_distance = new_distance
          target_vertex.predecessor = start_vertex
          heapq.heappush(self.heap, target_vertex)
      current_vertex.visited = True

  def find_shortest_path(self, end):
      print(
          f'The shortest path from {self.start.name} to {end.name} is {end.min_distance}')
      route = []
      current = end
      while current:
          route.append(current.name)
          current = current.predecessor
      route.reverse()
      print('->'.join(route))

  def yale_print(self, end):
    print(f'shortest path is {end.min_distance}')
    route = []
    current = end
    while current:
      route.append(current.name)
      current = current.predecessor
    route.reverse()
    print('->'.join(route))

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(5, nodeD)
nodeB.add_edge(13, nodeF)
nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)
nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)
nodeE.add_edge(10, nodeG)
nodeF.add_edge(12, nodeG)
nodeF.add_edge(4, nodeE)
nodeH.add_edge(2, nodeF)

start = nodeA
end = nodeE

example = Dijkstra()
example.calculate(start)
# example.find_shortest_path(end)
example.yale_print(end)