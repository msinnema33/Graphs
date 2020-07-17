# looking for the earliest ancestor so need a DFS.
    #need a queue and graph class

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size (self):
        return len(self.queue)    

class Graph:
    def __init__(self):
        self.verts = {} # adj list (dictionary) of vertices mapping labels to edges

    def add_vertex(self, vertex_id):
        if vertex_id not in self.verts:
            self.verts[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    # build graph to traverse
    g = Graph()
    # populate w verts
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
        # build edges
        g.add_edge(i[1], i[0])
    # init a Q and add starting vertex as a list
    q = Queue()
    q.enqueue([starting_node])
    # set max path and earliest ancestor -1 for return if no neighbors
    max_path = 1
    earliest = -1
    # while the Q has elements
    while q.size() > 0:
        # we pull the first element into our path
        path = q.dequeue()
        # set v to the last index of path
        v = path[-1]
        if(len(path) >= max_path and v < earliest) or (len(path) > max_path):
            earliest = v
            max_path = len(path)
        for next_item in g.verts[v]:
            copy = list(path)
            copy.append(next_item)
            q.enqueue(copy)
    return earliest

'''
Solution from Wednesday
'''
# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)
        
# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.vertices:
#             self.vertices[vertex] = set()

#     def add_edge(self, v1, v2):
#         self.vertices[v1].add(v2)

#     def get_neighors(self, vertex):
#         return self.vertices[vertex]

# ## Build a path like we did in search
# ## But we don't know when to stop until we've seen everyone
# def build_graph(ancestors):
#     graph = Graph()
#     for parent, child in ancestors:
#         graph.add_vertex(parent)
#         graph.add_vertex(child)
#         graph.add_edge(child, parent)
#     return graph

# def earliest_ancestor(ancestors, starting_node):
#     graph = build_graph(ancestors)
#     s = Stack()
#     visited = set()
#     s.push([starting_node])
#     longest_path = [starting_node]
#     aged_one = -1

#     while s.size() > 0:
#         path = s.pop()
#         current_node = path[-1]

#         # if path is longer, or path is equal but the id is smaller
#         if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
#             longest_path = path
#             aged_one = longest_path[-1]

#         if current_node not in visited:
#             visited.add(current_node)
#             parents = graph.get_neighors(current_node)

#             for parent in parents:
#                 new_path = path + [parent]
#                 s.push(new_path)

#     return aged_one
