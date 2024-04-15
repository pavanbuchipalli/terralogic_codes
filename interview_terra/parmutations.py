a = [1,2,3]
for i in  a:
    for j in a :
        if i != j:
            for k in a :
                if k != i and k != j:
                    print(i,j,k)
