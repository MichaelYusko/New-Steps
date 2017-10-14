import scipy as sp

# Read the file
data = sp.genfromtxt('web_traffic.tsv', delimiter='\t')


# Get vectors
x = data[:, 0]
y = data[:, 1]

# Get only an integers
x = x[~sp.isnan(x)]
y = y[~sp.isnan(y)]
