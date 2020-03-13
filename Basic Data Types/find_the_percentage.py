n = int(input())
a = {}
for x in range(n):
    val_1, val_2, val_3, val_4 = map(str, input().split())
    val_2 = float(val_2)
    val_3 = float(val_3)
    val_4 = float(val_4)
    k = (val_2 + val_3 + val_4)/3
    a.update({val_1:k})
o = input()
print(format(a[o],'.2f'))