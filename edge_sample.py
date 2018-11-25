import random
from collections import defaultdict

class EdgeSample:
    def __init__(self):
        self._S = []
        self._neighborhood = defaultdict(set)

    def add_edge(self,u,v):
        self._S.append((u,v))
        self.edit_neighborhood('+',u,v)

    def remove_random_edge(self):
        rand_choice = random.randint(0,len(self._S)-1)
        u_dash,v_dash = self._S.pop(rand_choice)
        self.edit_neighborhood('-',u_dash,v_dash)
        return u_dash, v_dash

    """def get_intersection_neighborhood(self,u,v):
        u_neighbors = set()
        v_neighbors = set()
        for edge in self._S:
            if u in edge or v in edge:
                if u in edge:
                    u_neighbors.add(edge[edge.index(u)-1]) # if index(u)=0, picks -1 and index(1), picks 0

                if v in edge:
                    v_neighbors.add(edge[edge.index(v)-1])
 
        return u_neighbors.intersection(v_neighbors)"""

    def get_intersection_neighborhood(self,u,v):
        if u in self._neighborhood and v in self._neighborhood:
            return self._neighborhood[u].intersection(self._neighborhood[v])
        else:
            return None


    def edit_neighborhood(self,op,u,v):
        if op == '+':
            self._neighborhood[u].add(v)
            self._neighborhood[v].add(u)

        elif op == '-':
            try:
                self._neighborhood[u].remove(v)
                self._neighborhood[v].remove(u)
            except:
                pass

            if not self._neighborhood[u]:
                self._neighborhood.pop(u)

            if not self._neighborhood[v]:
                self._neighborhood.pop(v)
