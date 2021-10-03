fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
lst = list()
for line in inp:
    line = inp.rstrip()
    words = line.split()

res = []
[res.append(x) for x in words if x not in res]

print(sorted(res))