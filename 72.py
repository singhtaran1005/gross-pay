# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for inp in fname:
    print(inp.isUpper())

