
import numpy as np

q_table = np.array([
    [0.1, 0.5, 0.2, 0.3],
    [0.4, 0.1, 0.8, 0.2],
    [0.2, 0.6, 0.3, 0.1]
])

print(q_table[1, 2])
print(q_table[0])
print(np.argmax(q_table[1]))
print(np.max(q_table[1]))
