 for i in range(1,6):
    for s in range(5-i,0,-1):
        print("-",end="")
    for j in range(i,i*2):
        print(j,end="")
    for j in range(i*2-1,i,-1):
        print(j,end="")
    print("")
    
