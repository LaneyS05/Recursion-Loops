for number in range(3):
    print("hello", number + 1, (number + 1) * ".")

# cleaner
for i in range(1, 4):
    print("wow", i, i * ".")

# step
for x in range(1, 10, 2):
    print("PY", x, x * ".")


for y in range (2, 10, 2):
    print(y)

count = 0
for num in range (1, 10):
     if num % 2 == 0:
        count +=1
        print(num)
print(f"we have {count} even numbers")
