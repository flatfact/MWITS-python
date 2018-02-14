f = open("data.txt")
print(sum(map(lambda x: float(x.strip().split(':')[3]),f.readlines())))