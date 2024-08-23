# the inner loop will be execute three times
# every time after the outer loop has execute

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


for sum in range(5):
    sum += sum
    print(sum)


num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)
