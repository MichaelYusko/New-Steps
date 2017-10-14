import scipy as sp
import matplotlib.pyplot as plt

# Read the file
data = sp.genfromtxt('web_traffic.tsv', delimiter='\t')

# Get vectors
x = data[:, 0]
y = data[:, 1]

sp.sum(sp.isnan(x))

# Get only an integers
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

x.shape, y.shape
plt.scatter(x, y, s=10)
plt.title('Web traffic over the last month')
plt.xlabel('Time')
plt.ylabel('Hits/hours')
plt.xticks([w * 7 * 24 for w in range(10)],
            ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')
plt.show()