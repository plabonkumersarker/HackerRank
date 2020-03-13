n = int(input())
li = []

numList = list(map(int,input().strip().split()))[:n]

numList.sort()

p = numList[n-1]

for x in numList:
	if p != x:
		li.append(x)
k = numList.count(p)
print(li[n-(k+1)])

