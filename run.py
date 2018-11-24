from triest_base import TriestBase

debug = False

if not debug:
    filename = "./data/ca-AstroPh.txt"
    M = 10000
else:
    filename = "./data/dummy.txt"
    M = 6

base = TriestBase(M)

with open(filename) as f:
    for line in f:
        if line.startswith('#'):
            continue
        
        u,v = list(map(int,line.strip().split()))
        base.run(u,v)

    print("============ FINAL OUTPUT IS ====================")
    print(base.return_counters())
