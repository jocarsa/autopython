import numpy as np
import time

# Create two large arrays
size = 3000
a = np.arange(size)
b = np.arange(size)

# Measure time of outer product (similar to nested loop multiplication)
start = time.time()

result = np.outer(a, b)  # Equivalent to [[i * j for j in b] for i in a]

end = time.time()
print(f"Time taken with NumPy: {end - start:.4f} seconds")
