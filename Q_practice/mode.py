n = 333113322244444444444444444444444
n = list(str(n))
db = {}
print(n)
for digit in n:
    if digit in db:
        db[digit] = db[digit]+1
    else:
        db[digit] = 1
key = list(db.keys())

val = list(db.values())
m = max(val)
#print(m)

pos = 0
for k in key:
    if m == db[k]:
        print(key[pos])
    else:
        pos = pos+1
