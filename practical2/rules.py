def checkSpecies(dataset):
    species = lambda x : x in ['setosa', 'versicolor', 'virginica']
    return dataset['Species'].apply(species)

def checkPositive(dataset):
    positive = lambda x : x[0:] > 0
    return dataset[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']].apply(positive, axis = 1)

def checkPetal(dataset):
    double = lambda x : x[0] >= 2 * x[1]
    return dataset[['Petal.Length', 'Petal.Width']].apply(double, axis = 1)

def checkSepal(dataset):
    length = lambda x : x <= 30
    return dataset['Sepal.Length'].apply(length)

def sepalsLonger(dataset):
    length = lambda x : x[0] > x[1]
    return dataset[['Sepal.Length', 'Petal.Length']].apply(length, axis = 1)