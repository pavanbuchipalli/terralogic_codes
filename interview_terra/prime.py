for j in range(1,32):
    f=0
    for i in range(2,j):
        if (j%i) == 0:
            f =1
    if f==0 :
        print(j,"it is ")
    else:
        print(j,"it is  not")
