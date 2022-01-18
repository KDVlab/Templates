#Sample code for smoothing data and taking a derivative or two. Note that this is probably bad and inefficient and you probably should just use https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html

import numpy as np
import matplotlib.pyplot as plt
#this function takes an x and y data array and smooths the y data, and spits out the corresponding x and y arrays.\
# It's averaged over an interval of avg_interval (has to be odd integer) by fitting a 1-degree polynomial to the data, filling out the optional argument allows you to change this
def smooth_n_derive(x, y, avg_interval, derive = False, polynomial = 1):
    newx =[]
    newy = []
    half_interval = int(avg_interval/2 + 0.5)
    if derive == True:
        y = np.gradient(np.asarray(y), np.asarray(x))
    for m in range(len(x)-avg_interval):
        p = np.polyfit(x[m:m+avg_interval], y[m:m+avg_interval], polynomial)
        y_temp = np.polyval(p,x[m+half_interval])
        newy.append(y_temp)
        newx.append(x[m+half_interval])
    return newx, newy

##test data to show how to use it
testdatax = np.linspace(0,2*np.pi,100)
testdatay = np.sin(testdatax) + np.random.random(100) * 0.2
smoothx, smoothy = smooth_n_derive(testdatax, testdatay, 5)
smoderx, smodery = smooth_n_derive(testdatax, testdatay, 5, derive = True)

fig, ax = plt.subplots()
ax.plot(testdatax, testdatay, '.')
ax.plot(smoothx, smoothy , '-')
ax.plot(smoderx, smodery , '-')
plt.show()
