name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
hours = list()
hour = list()
tmp = list()
for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    hour = line[0]
    counts[hour] = counts.get(hour, 0) + 1

for hour, counts in counts.items():
    newt = (hour, counts)
    tmp.append(newt)

tmp = sorted(tmp)

for hour, counts in tmp:
    print(hour, counts)
