import pandas as pd
df = pd.read_csv('practical1.txt', sep=' ')

def ageRange(df):
    age_range = lambda r : r in range(151)
    result = df['Age'].apply(age_range)
    # print(result)
    # print(df[result])
    return df[result]

def ageGreaterThanYearsMarried(df):
    age_greater_than_yearsmarried = lambda x : x['Age'] > x['yearsmarried']
    result = df[['Age', 'yearsmarried']].apply(age_greater_than_yearsmarried, axis = 1)
    # print(result)
    # print(df[result])
    return df[result]

def checkStatus(df):
    status = lambda x : x == 'married' or x == 'single' or x == 'widowed'
    result = df['status'].apply(status)
    # print(result)
    # print(df[result])
    return df[result]


def checkAgeGroup(df):
    def age_group(x):
        if (x['Age'] < 18 and x['agegroup'] == 'child'):
            return True
        elif ((x['Age'] > 18 and x['Age'] < 65) and x['agegroup'] == 'adult'):
            return True
        elif (x['Age'] > 65 and x['agegroup'] == 'elderly'):
            return True
        else:
            return False
    result = df[['Age', 'agegroup']].apply(age_group, axis = 1)
    # print(result)
    # print(df[result])
    return df[result]

# df = ageRange(df)

# df = ageGreaterThanYearsMarried(df)

# df = checkStatus(df)

# df = checkAgeGroup(df)
print('-' * 15, 'Original Data', '-' * 10)
print(df)
print('-' * 50)

print('-' * 15, 'Age in range 0-150', '-' * 10)
print(ageRange(df))
print('-' * 50)

print('-' * 15, 'Age greater than years married', '-' * 10)
print(ageGreaterThanYearsMarried(df))
print('-' * 50)

print('-' * 15, 'Status should be married or single or widowed', '-' * 10)
print(checkStatus(df))
print('-' * 50)

print('-' * 15, 'Age Group', '-' * 10)
print(checkAgeGroup(df))
print('-' * 50)