for i in range(0,21,5):
    print(i)
for i,j in (('apple',5),('banana',7),('melon',10)):
    print('%s, %d yuan'%(i,j))
for i,j in zip(('banana','apple','orange'),(5,7,10)):
    print('%s, %d yuan'%(i,j))
for i in ((1,2),(3,4)):
    print(i[0]*i[1])