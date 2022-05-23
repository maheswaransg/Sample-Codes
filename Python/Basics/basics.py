# Foor loop
for i in range(100) : 
    print(i)
for j in [1,2,3] : 
    print(j)
for k in ['one', 'Two', 'Three'] :
    print(k)

inc = 2
for l in range(1, 6) :
    for m in range(1, inc) :
        print(l, end =" ")
    print(' ')
    inc += 1

inc = 6
for l in range(5, 0, -1) :
    for m in range(1, inc) :
        print(l, end =" ")
    print(' ')
    inc -=1

