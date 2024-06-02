data = []
with open("5.3.kids.txt", "r", encoding="utf-8") as file:
    for line in file.read().splitlines():
        temp = line.split()
        temp[2] = int(temp[2])
        data.append(temp)
data.sort(key=lambda x: x[2])
with open("5.3.youngestkid.txt", "w", encoding="utf-8") as file:
    data[0][2] = str(data[0][2])
    file.write(" ".join(data[0]))
with open("5.3.eldestkid.txt", "w", encoding="utf-8") as file:
    data[-1][2] = str(data[-1][2])
    file.write(" ".join(data[-1]))