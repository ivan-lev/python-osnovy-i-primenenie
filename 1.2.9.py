objects = [1, 2, 1, 2, 3]
ans = 0
a = []
for i in range(len(objects)): # доступная переменная objects
    if objects[i] not in a:
        a.append(objects[i])
ans = len(a)
print(ans)
