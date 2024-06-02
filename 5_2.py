data = []   
with open("5.2.input.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()
data.sort()
with open("5.2.output.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(data))