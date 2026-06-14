with open("input.txt","r") as f:
    rows = int(f.readline().strip())

for i in range(1, rows + 1):
    print("* " * i)

    