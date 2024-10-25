from edge import Edge
class Graph:
    #словарик для списка смешности
    def __init__(self):
        self.adjacency_list = {}

    #функция для добавления ребра
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.adjacency_list:
            self.adjacency_list[from_node] = []
        self.adjacency_list[from_node].append(Edge(to_node, weight))

    #функция для получения соседей
    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])
