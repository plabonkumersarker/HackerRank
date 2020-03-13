n = int(input())
li = [int(x) for x in input().split()]
t = tuple(li)
print(hash(t))