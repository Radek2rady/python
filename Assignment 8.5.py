fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("From:"):
        line = line.split(":")
        mail = line[1]
        mail = mail.strip()
        count = count + 1
        print(mail)


if len(fname) < 1 : fname = "mbox-short.txt"


print("There were", count, "lines in the file with From as the first word")
