largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inp=float(num)
    except:
        print("Invalid input")
    if smallest is None:
        smallest=inp    
    elif inp < smallest:
        smallest=inp
    elif inp>largest:
        largest=inp

    continue

print("Maximum", largest)
print("Minimum", smallest)
