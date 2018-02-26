s = 0
n = 0
while 1 == 1:
    x = input()
    if x == 'stop':
        print(s/n)
        break
        
    else:
        s = s+len(x)
        n = n+1
