a = 120
b = 120

print(a)
print(b)

a,b = b,a
print(a,b)

if a<b:
    print("а меньше б")
elif a==b:
    print("а равно б")
else:
    print("а больше б")

