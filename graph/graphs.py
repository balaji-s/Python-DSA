class vertex:
    '''
    creates a vertex class 
    '''
    def __init__(self, key):
        self.key = key
        self.connected_to = {}
    
    def add_weight(self, branch, weight = 0):
        self.connected_to[branch] = weight
    
    def get_key(self):
        return self.key

    def get_weight(self, branch):
        return self.connected_to[branch]

    def get_connections(self):
        return self.connected_to.keys()

    def __str__(self):

        return str(self.key) + 'connected to' +str([x.id for x in self.connected_to])

class Graph:

    def __init__(self):

        self.vertices_list = {}
        self.num_of_vertices = 0
    
    def add_vertex(self, key):
        self.num_of_vertices += 1
        new_vertex = vertex(key)
        self.vertices_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices_list:
            return self.vertices_list[n]
        else:
            return None
    
    def __contains(self, n):
        return n in self.vertices_list

    def add_edge(self, f, t, cost = 0):
        if f not in self.vertices_list:
            nv = self.add_vertex(f)
        if t not in self.vertices_list:
            nv = self.add_vertex(t)
        self.vertices_list[f].add_weight(self.vertices_list[t],cost)
    
    def get_vertices(self):
        return self.vertices_list.keys()

    def __iter__(self):
        return iter(self.vertices_list.values())


graph = Graph()

for i in range(6):
    graph.add_vertex(i)

graph.add_edge(0, 1, 5)

    
    
