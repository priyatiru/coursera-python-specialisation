largest= None
smallest=None
while True:
    num=input("Enter a number: ")
    if num=="done":
        break
    try:
        numint=int(num)
        if largest is None:
            largest=numint
        elif largest < numint:
            largest = numint
        if smallest is None:
            smallest=numint
        elif smallest > numint:
            smallest = numint
    except:
        print("Invalid input")
    continue
print("Maximum is ",largest)
print("Minimum is ",smallest)
