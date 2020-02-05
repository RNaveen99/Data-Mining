import numpy as np
import pandas as pd
import rules
dataset = pd.read_csv('dirty_iris.csv')
dataset = dataset.replace([np.inf, -np.inf], np.nan)

newDataset = dataset.dropna()

percentage = (newDataset.shape[0] / dataset.shape[0]) * 100



print(percentage)
print(dataset)
print(rules.checkSpecies(dataset))
print(rules.checkPositive(dataset))
print(rules.checkPetal(dataset))
print(rules.checkSepal(dataset))