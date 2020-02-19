import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('practical1.txt', sep=' ')

def ageRange(dataset):
    age_range = lambda r : r in range(151)
    result = dataset['Age'].apply(age_range)
    return result
    # return dataset[result]

def ageGreaterThanYearsMarried(dataset):
    age_greater_than_yearsmarried = lambda x : x['Age'] > x['yearsmarried']
    result = dataset[['Age', 'yearsmarried']].apply(age_greater_than_yearsmarried, axis = 1)
    return result
    # return dataset[result]

def checkStatus(dataset):
    status = lambda x : x == 'married' or x == 'single' or x == 'widowed'
    result = dataset['status'].apply(status)
    return result
    # return dataset[result]


def checkAgeGroup(dataset):
    def age_group(x):
        if (x['Age'] < 18 and x['agegroup'] == 'child'):
            return True
        elif ((x['Age'] >= 18 and x['Age'] < 66) and x['agegroup'] == 'adult'):
            return True
        elif (x['Age'] > 65 and x['agegroup'] == 'elderly'):
            return True
        else:
            return False
    result = dataset[['Age', 'agegroup']].apply(age_group, axis = 1)
    return result
    # return dataset[result]

a = ageRange(dataset)
b = ageGreaterThanYearsMarried(dataset)
c = checkStatus(dataset)
d = checkAgeGroup(dataset)

datasetRules = {0 : a, 1 : b, 2 : c, 3 : d}

X = [True] * len(dataset)

rulesBrokenCount = np.empty(len(datasetRules))

for i in datasetRules:
    rulesBrokenCount[i] = len(datasetRules[i]) - datasetRules[i].value_counts().at[True]
    X = X & datasetRules[i]

for i in range(len(rulesBrokenCount)):
    print(f'Rule {i + 1} invalidation =  {int(rulesBrokenCount[i])} times')

r = np.array(['rule1', 'rule2', 'rule3', 'rule4'])

plt.bar(r, rulesBrokenCount)
plt.xlabel('Rules')
plt.ylabel('Count of Rules Broken')
# dataset.boxplot()
plt.show()