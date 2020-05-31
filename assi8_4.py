fname=input("Enter a file name: ")
fh=open(fname)
x=list()
for line in fh:
    line=line.split()
    #print(line)
    for element in line:
        if element in x:
            continue
        else :
            x.append(element)
x.sort()
print(x)
