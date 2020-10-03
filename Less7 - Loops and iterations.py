line = "--------------------------------------"
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print("Found")
        break
    print(num)

print(line)

for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)

print(line)

for num in nums:
    for letter in "abc":
        print(num, letter)

print(line)

for i in range(5, 10):
    print(i)

print(line)

###### while loops go on until contition is met, or until a break
x = 1
while x < 10:
    print(x)
    x += 1

print(line)

x = 1
while True:
    if x == 10:
        print("Found")
        break
    print(x)
    x += 1

print(line)
