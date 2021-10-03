name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
counts = dict()
words = dict()
for line in handle:
    if line.startswith('From '):
        line = line.split()
        lst.append(line[1])

for word in lst:
    counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword, bigcount)