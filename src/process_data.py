# this is a test
#This is a 2nd test



from benfordslaw import benfordslaw
import pandas as pd

# Initialize
bl = benfordslaw(alpha=0.05, method='ks')

""" # get test data
with open('src/testData.txt') as raw:
    D = raw.read()

X = D.split('\n')

while (X[-1] == ''):
    del X[-1]


for index in range(0, len(X)):
    X[index] = int(X[index]) """

""" # Load elections example
df = bl.import_example(data='USA')

# Extract election information.
X = df['votes'].loc[df['candidate']=='Donald Trump'].values
 """

X = pd.read_csv('src/testData.txt')

# Print
print(X)
# array([ 5387, 23618,  1710, ...,    16,    21,     0], dtype=int64)

# Make fit
results = bl.fit(X)
print(results)
# Plot
bl.plot(title='Donald Trump')