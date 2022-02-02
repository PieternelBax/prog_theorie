import matplotlib.pyplot as plt
import numpy as np

# load file
file = np.loadtxt('random_solutions6x6_2.txt', unpack='False')

plt.hist(file, histtype='bar', bins = np.arange(min(file), max(file) + 200, 200), edgecolor='black')
plt.xlabel('Total Moves')
plt.ylabel('Frequency')
plt.title('Distribution of Random Solver')
plt.show()
