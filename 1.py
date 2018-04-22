N = int(input())
x = 0
M = []
M2 = []
FR = []
while x < N:
	M.append(input().split())
	FR.append(M[x][0])
	del M[x][0]
	del M[x][0]
	x += 1
x = 0
while x < N:
	y = 0
	while y < N:
		if y != x and (FR[x] in M[y]):
			M[y].remove(FR[x])
		y += 1
	x += 1
x = 0
while x < N:
	y = 0
	while y < len(M[x]):
		M2.append(M[x][y])
		y += 1
	x += 1
x = 0
while x < len(M2):
	if M2.count(M2[x]) > 1:
		M2.remove(M2[x])
	else:
		x += 1
FR2 = len(M2)
print(FR2)
