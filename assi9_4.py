# open file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
# extract all the addresses in to a list
lst = list()
for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1
#count andn print
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword,bigcount)
