import random
from edge_sample import EdgeSample
from collections import defaultdict

class TriestBase:
    def __init__(self,M):
        self._M = M
        self._sample = EdgeSample()
        self._globalT = 0
        self._localT = {}
        self._t = 0

    def sample_edge(self,u,v):
        if self._t <= self._M:
            return True
        elif self.flip_biased_coin():
            u_dash, v_dash = self._sample.remove_random_edge()
            self.update_counters(u_dash,v_dash,'-')
            return True
        return False

    def update_counters(self,u,v,op):
        common_neighborhood = self._sample.get_intersection_neighborhood(u,v)
        
        if not len(common_neighborhood):
            return

        for c in common_neighborhood:

            if op == '+':
                self._globalT += 1
                
                if c in self._localT:
                    self._localT[c] += 1
                else:
                    self._localT[c] = 1

                if u in self._localT:
                    self._localT[u] += 1
                else:
                    self._localT[u] =1

                if v in self._localT:
                    self._localT[v] += 1
                else:
                    self._localT[v] = 1

            elif op == '-':
                self._globalT -= 1
                
                self._localT[c] -= 1

                if self._localT[c] == 0:
                    self._localT.pop(c)

                self._localT[u] -= 1
                
                if self._localT[u] == 0:
                    self._localT.pop(u)

                self._localT[v] -= 1
                if self._localT[v] == 0:
                    self._localT.pop(v)


    def flip_biased_coin(self):
        head_prob = random.random()

        if head_prob <= self._M/self._t:
            return True
        else:
            return False

    def return_counters(self):
        estimate = max(1, (self._t * (self._t - 1) * (self._t - 2))/(self._M * (self._M - 1) * (self._M - 2)))
        
        return {'global':int(estimate * self._globalT),'local':self._localT}

    def run(self,u,v):
        self._t += 1
        print("============RUN {} START============".format(self._t))
        print("u: {} and v: {}".format(u,v))
        if self.sample_edge(u,v):
            self._sample.add_edge(u,v)

        print("============RUN {} END============".format(self._t))
