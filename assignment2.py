

rollnumber = 1024170124

L = []
for digit in str(rollnumber):
    L.append(int(digit) * 10)

print("Q1 ")
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
newlist = [x for x in L if x > average]
print(newlist)

print("\n Q2 ")

scores = tuple(L[:8])
print("Scores:", scores)

high = max(scores)
low = min(scores)

print("Highest ", high)
print("Highest index ", scores.index(high))
print("Lowest ", low)
print("Lowest count ", scores.count(low))

reversedscores = list(scores[::-1])
print("Reversed:", reversedscores)

score = int(input("Enter a score "))
if score in scores:
    print("Index:", scores.index(score))
else:
    print("not present")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

print("tuples are immutable so their elements cannot be changed")

first, second, *remaining = scores
print(first, second, remaining)

print("\nQ3")

random.seed(rollnumber)
numbers = [random.randint(100, 900) for i in range(100)]

odd = [x for x in numbers if x % 2 != 0]
even = [x for x in numbers if x % 2 == 0]

print("Odd numbers ", odd)
print("Odd count ", len(odd))
print("Even numbers ", even)
print("Even count ", len(even))

primes = [x for x in numbers if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]
print("Prime numbers ", primes)
print("Prime count ", len(primes))

most = max(set(numbers), key=numbers.count)
print("Most frequent:", most)
print("Frequency ", numbers.count(most))

print("\n Q4")

digits = [int(x) for x in str(rollnumber)[:8]]

A = {x * 7 for x in digits}
B = {x * 9 for x in digits}

print("A", A)
print("B ", B)

print("Union", A.union(B))
print("Intersection ", A.intersection(B))
print("A-B", A.difference(B))
print("B-A", B.difference(A))
print("Symmetric difference", A.symmetric_difference(B))
print("A subset of B:", A.issubset(B))
print("B superset of A", B.issuperset(A))

X = int(input("Enter X: "))
A.discard(X)
print("A after discard:", A)
print("discard() is safer because it does not give an error if the value is absent.")

print("\n Q5")

name = input("Enter your name ")
branch = input("Enter your branch")
age = int(input("Enter your age: "))
city = input("Enter your home city: ")
cgpa = float(input("Enter your CGPA "))

mydict = {
    "name": name,
    "roll_no": rollnumber,
    "branch": branch,
    "age": age,
    "city": city
}

mydict["location"] = mydict.pop("city")
mydict["cgpa"] = cgpa
mydict["age"] = mydict["age"] + 1

print(mydict)

d1 = mydict.copy()
d1.pop("branch")
print(d1)

d2 = mydict.copy()
del d2["branch"]
print(d2)

print("pop() returns the removed value, while del only deletes the key.")

for key, value in mydict.items():
    print(key, "→", value)

if "email" in mydict:
    print(mydict["email"])
else:
    print("email not present")

friend_dict = {
    "name": "archit",
    "roll_no": 1024170124,
    "branch": "CSE",
    "age": 19,
    "city": "Delhi"
}

merged = {**mydict, **friend_dict}
print(merged)
print("when keys are the same, values from the second dictionary win")

string_dict = {k:  v for k, v in mydict.items() if isinstance(v, str)}
print(string_dict)
