import os
import matplotlib.pyplot as plt
from pylab import plot, show, savefig
from random import normalvariate

path = "/home/dcl253/quant-econ/dlau"
ts_length = 100
os.chdir(path)

epsilon_values = []   # An empty list
for i in range(ts_length):
    e = normalvariate(0, 1)
    epsilon_values.append(e)
plot(epsilon_values, 'b-')
show()
os.getcwd()
savefig('graph.png')

# fig= plt.figure()
# #ax = fig.add_subplot(epsilon_values, 'b-')
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(range(100))
# fig.savefig('foo.png')
print " end "
