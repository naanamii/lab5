prod = 1
with open("5.1.input.txt", "r", encoding="utf-8") as file:
    data = list(map(int, file.readline().split()))
    for num in data:
        prod *= num
with open("5.1.output.txt", "w", encoding="utf-8") as file:
    file.write(str(prod))