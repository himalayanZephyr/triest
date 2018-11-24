from triest_base import TriestBase
from triest_impr import TriestImpr

debug = False
mode = 2

if not debug:
    filename = "./data/ca-AstroPh.txt"
    M = 1000
else:
    filename = "./data/dummy.txt"
    M = 7

if mode == 1:
    model = TriestBase(M)
else:
    model = TriestImpr(M)

with open(filename) as f:
    for line in f:
        if line.startswith('#'):
            continue
        
        u,v = list(map(int,line.strip().split()))
        model.run(u,v)

    print("============ FINAL OUTPUT IS ====================")
    print(model.return_counters())
