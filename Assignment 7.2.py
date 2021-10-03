# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
x = 0
numbers = []
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        host = line.split(":")[1]
        host = host.strip()
        if host.startswith("0."):
            count = count + 1
        host = float(host)
        print(dir(host))
        x = host + x
#        numbers.append(host)
        output = x / count
#        print(count)
    if not line.startswith("X-DSPAM-Confidence:") : continue
print("Average spam confidence:",+ output)
