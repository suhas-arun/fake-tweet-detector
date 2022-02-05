# this is a test
#This is a 2nd test



from benfordslaw import benfordslaw

# Initialize
bl = benfordslaw(alpha=0.05)

# get test data
X = []
with open('testData.txt') as raw:
    X.append(raw.readline)

# Print
print(X)
# array([ 5387, 23618,  1710, ...,    16,    21,     0], dtype=int64)

# Make fit
results = bl.fit(X)
print(results)
# Plot
bl.plot(title='Donald Trump')