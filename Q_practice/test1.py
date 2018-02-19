def p_dist(x,y,p=2):
    z = 0
    for i in range(len(x)):
        z = z+abs(x[i]-y[i])**p
    return z**(1/p)
x=(3.0,6.0,1.5)
y=(0.0,2.0,6.5)
p=3
print(p_dist(x,y,p))