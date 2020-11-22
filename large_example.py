import numpy as np

from ant_colony import AntColony

large_distances = np.random.randint(1,10,size=(100,100))
large_distances = (large_distances+large_distances.T).astype('float64')
np.fill_diagonal(large_distances,float('inf'))

large_ant_colony = AntColony(large_distances, 10, 10, 100, 0.15, alpha=1, beta=1)
print(large_ant_colony.run())