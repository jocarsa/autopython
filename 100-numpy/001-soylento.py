import time

# Create two large lists
size = 3000
a = [i for i in range(size)]
b = [j for j in range(size)]

# Measure time of a nested loop (simulating a matrix multiplication)
start = time.time()

result = []
for i in a:
    row = []
    for j in b:
        row.append(i * j)
    result.append(row)

end = time.time()
print(f"Time taken: {end - start:.2f} seconds")
