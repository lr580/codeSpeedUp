[False for i in range(3)]
[x for x in range(5)]
[print(i*i) for i in range(9)]
[float(input('input %d-th number:'%i)) for i in range(1,6)]
[x for x in range(13) if x%4==0]
[x*y for x in range(1,4) for y in range(10,31,10)]
[x+y+z for x in 'AB' for y in 'ab' for z in '12']
[i+1 for i in [j*(j+1) for j in range(11)]]
[[j**2 for j in range(i*3,i*3+3)] for i in range(3)]
{i:i**i for i in range(5)}
tuple(i for i in range(5))
(i for i in range(5))