import sys

file = sys.argv[1]
n = int(sys.argv[2])

with open(file, 'r') as f:
    # read first n lines
    for i in range(n):
        print(f.readline().strip())