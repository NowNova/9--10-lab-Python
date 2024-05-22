import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

speciescolumn = iris[:, 4]

uniqueSpecies, counts = np.unique(speciesColumn, return_counts=True)

print()
for species, count in zip(uniqueSpecies, counts):
    print(f'{species.decode("utf-8")}: {count}')