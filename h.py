number = 1024170124
L = []

for digit in str(number):
    L.append(int(digit) * 10)

print(L)

L.append(50)
print(L)

L.insert(2, 30)
print(L)

L.remove(70)
print(L)

L.pop()
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

print(L[:3])
print(L[-3:])

average = sum(L) / len(L)
print(average)

newlist = [x for x in L if x > average]
print(newlist)