def shoot(idx):
    if 0 <= idx < len(numbers):
        shot_value = numbers[idx]
        numbers[idx] = -1

        for count, item in enumerate(numbers):
            if item == -1:
                continue

            if item > shot_value:
                numbers[count] -= shot_value

            elif item <= shot_value:
                numbers[count] += shot_value


numbers = [int(x) for x in input().split()]
index = input()

while index != "End":
    index = int(index)

    shoot(index)

    index = input()

print(f"Shot targets: {numbers.count(-1)} -> ", end="")
print(*numbers, sep=" ")