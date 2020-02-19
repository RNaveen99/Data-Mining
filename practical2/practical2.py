import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import rules

dataset = pd.read_csv('dirty_iris.csv')
print(dataset)

completeObservations = len(dataset.dropna())
percentageOfCompleteObservation = (completeObservations / len(dataset)) * 100

print(f'Number of complete observations = {completeObservations}')
print(f'Percentage of complete observations = {percentageOfCompleteObservation}')

newDataset = dataset.replace([np.inf, -np.inf], np.nan)
newDataset[newDataset.iloc[:, :4] < 0] = np.nan
print(newDataset)

a = rules.checkSpecies(dataset)
b = rules.checkPositive(dataset)
b = b.iloc[0:, 0:].apply(lambda x: x[0] and x[1] and x[2] and x[3], axis = 1)
c = rules.checkPetal(dataset)
d = rules.checkSepal(dataset)
e = rules.sepalsLonger(dataset)

datasetRules = {0 : a, 1 : b, 2 : c, 3 : d, 4 : e}

X = [True] * len(dataset)

rulesBrokenCount = np.empty(len(datasetRules))

for i in datasetRules:
    rulesBrokenCount[i] = len(datasetRules[i]) - datasetRules[i].value_counts().at[True]
    X = X & datasetRules[i]

for i in range(len(rulesBrokenCount)):
    print(f'Rule {i + 1} invalidation =  {int(rulesBrokenCount[i])} times')

r = np.array(['rule1', 'rule2', 'rule3', 'rule4', 'rule5'])

plt.bar(r, rulesBrokenCount)
plt.xlabel('Rules')
plt.ylabel('Count of Rules Broken')
dataset.boxplot()
plt.show()