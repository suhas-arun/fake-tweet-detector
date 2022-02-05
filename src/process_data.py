# this is a test
#This is a 2nd test



from benfordslaw import benfordslaw
import pandas as pd

# Initialize
bl = benfordslaw(alpha=0.05, method='ks')

""" # get test data
with open('src/testData.txt') as raw:
    D = raw.read()

X = D.split(',\n')

while (X[-1] == ''):
    del X[-1]


for index in range(0, len(X)):
    X[index] = int(X[index])
data = pd.array(X) """

""" # Load elections example
df = bl.import_example(data='USA')

# Extract election information.
data = df['votes'].loc[df['candidate']=='Donald Trump'].values """


#data = pd.read_csv('src/testData.txt',header=0)
X = pd.DataFrame({'followers':[1,1,1,1,1,1,1,11,1,1,1, 2,2,2,2,2,2,2,2222,2,22,2,2,2,22,2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 8,9]})
data = X['followers']
# Print
print(data)
# array([ 5387, 23618,  1710, ...,    16,    21,     0], dtype=int64)

# Make fit
results = bl.fit(data)
print(results)
# Plot
bl.plot(title='Donald Trump')