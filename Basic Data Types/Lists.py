n = int(input())
x = []
for p in range(n):
    a = input().split(' ')

    if a[0] == "insert":
        a[2] = int(a[2])
        a[1] = int(a[1])
        x.insert(a[1], a[2])
    elif a[0] == "print":
        print(x)
    elif a[0] == "remove":
        a[1] = int(a[1])
        x.remove(a[1])
    elif a[0] == "append":
        a[1] = int(a[1])
        x.append(a[1])
    elif a[0] == "sort":
        x.sort()
    elif a[0] == "pop":
        x.pop()
    elif a[0] == "reverse":
        x.reverse()