"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() #set of edges

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        #mark visited nodes
        visited = set()
        #until queue is empty
        while q.size() > 0:
            v = q.dequeue() # deQ first node
            if v not in visited:
                print(v)
                visited.add(v) #mark as visited
                for next_vertex in  self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        #literaly same as above but with a stack instead of Q
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)


    def dft_recursive(self, starting_vertex, visited=None):
        # if we instantiate visited as a set (visited = set())
        # we can take out the next two lines
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for next_vertex in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        #push start of path into Queue
        q.enqueue([starting_vertex])
        while q.size() > 0:
            # get first path from Queue
            path = q.dequeue()
            #get last vertex from path
            last_vert = path[-1]
            # path found
            if last_vert == destination_vertex:
                return path
            # enumerate all adjacent nodes, build a new path, and push into Q
            for adjacent in self.get_neighbors(last_vert):
                new_path = list(path)
                new_path.append(adjacent)
                q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        path = []
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            #grab first vertex
            v = s.pop()
            if v not in visited:
                # print(v)
                #mark visited
                visited.add(v)
                #add to path
                path.append(v)
                if v == destination_vertex:
                    return path
                    
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[]):
        if starting_vertex == destination_vertex:
            print('target found!', starting_vertex)
            return visited + [starting_vertex]
        else:
            visited.append(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                print(f'{edge} is a neighbor to {starting_vertex}:{self.get_neighbors(starting_vertex)}')
                if edge not in visited:
                    print(f'{edge} not in visited, recurse, append {starting_vertex} if not in list')
                    path = self.dfs_recursive(edge, destination_vertex, visited)
                    if path:
                        print('path is', path)
                        return path
            visited.remove(starting_vertex)
            print(f'Delete: {starting_vertex} its exit {edge} has been visited and no path to {destination_vertex} was found')

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))