from triest_base import TriestBase
from triest_impr import TriestImpr

debug = False
mode = 2

if not debug:
    filename = "./data/out.ca-AstroPh"
    M_vals = [7000]#[1000, 3000, 5000, 7000, 9000, 10000, 12000]
else:
    filename = "./data/dummy.txt"
    M_vals = [7]

output_vals = []

iterations = 10

for M in M_vals:
    if mode == 1:
        model = TriestBase(M)
    else:
        model = TriestImpr(M)

    with open(filename) as f:
        for line in f:
            if line.startswith('%'):
                continue
        
            u,v = list(map(int,line.strip().split()))
            model.run(u,v)

        print("============ FINAL OUTPUT IS ====================")
        print(model.return_counters())

        #output_vals.append(model.return_counters()['global'])

#print("Output vals",output_vals)
