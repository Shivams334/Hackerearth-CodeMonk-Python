T=int(raw_input())
while T>0:
    a1=list(raw_input().split())
    a2=list(raw_input().split())
    x=list()
    for i in a2:
        x.append(int(bin(int(i)).count('1')))
    x.sort()
    c=0
    i=int(a1[0])-1
    s=int(a1[1])
    while s>0:
        c=c+x[i]
        i=i-1
        s=s-1
    print c
    T=T-1
