import matplotlib.pyplot as plt
import numpy as np


n = 5  
grid = np.zeros((n, n))  
initial_state = (0, 0)  
final_state = (4, 4)    
obstacles = [(1, 4), (2, 2), (3, 1)]  
weights = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])
fig, ax = plt.subplots()
ax.matshow(np.ones((n, n)), cmap='gray', alpha=0.2)
for i in range(n):
    for j in range(n):
        if (i, j) == initial_state:
            ax.text(j, i, 'I', va='center', ha='center', color='black', fontsize=11, fontweight='bold')  
        elif (i, j) == final_state:
            ax.text(j, i, 'F', va='center', ha='center', color='black', fontsize=11, fontweight='bold')  
        elif (i, j) in obstacles:
            ax.text(j, i, 'X', va='center', ha='center', color='purple', fontsize=9, fontweight='bold')  
        else:
            ax.text(j, i, f'{weights[i, j]}', va='center', ha='center', color='green')  
ax.set_xticks(np.arange(n))
ax.set_yticks(np.arange(n))
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.grid(False)
plt.show()