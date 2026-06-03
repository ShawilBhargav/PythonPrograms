a = [1,233,24,2,4,2,2,4,3]
visited = []
for i in range(len(a)):
    if a[i] in visited:
        continue
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    print(f"{a[i]} -> {count} times")
    visited.append(a[i])