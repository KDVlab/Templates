#Written for python 3.6
import matplotlib
matplotlib.rc('text', usetex = True) #this makes matplotlib use the latex renderer
import matplotlib.pyplot as plt
import numpy as np

gamma = 72e-3 #(mN/m)
data_x = np.linspace(0,800e-6) #making some sample data
data_y =(2*gamma**1.5*data_x/(1000*1)**0.5 - 1000*data_x**4 - np.pi*gamma*data_x**2)/4.11e-21


figure = plt.figure(1) #Makes a matplotlib figure, the 1 indicates the plot number, plotting more figures at once requires changing that number

figure.subplots_adjust(top=0.96, bottom=0.2, left=0.16, right=0.96) # adjusts the margins of the plot
axes = figure.add_subplot(111) # This allows for a subplot to be generated. More
axes.plot(data_x, data_y,'*', color = 'k', label = r'$\textrm{sin}\left(x\right)$') # plotting the data, with a label for the legend, marker style *, color black, using an r before a string allows for the latex text renderer.
axes.set_xlabel(r'$X \textrm{data}$', fontsize = 18) #x and y axis labels
axes.set_ylabel(r'$Y \textrm{data}$', fontsize = 18)
axes.tick_params(labelsize = 20)
axes.legend(loc = 3, fontsize = 16, frameon = False)
plt.show()

'''
# Figures with sequential data: using colourmaps

#Here we'll look at plotting the data using a colourmap
ra = np.r_[np.linspace(0,0.9, len(x))]
c = plt.get_cmap("plasma") #I like using sequential colourmaps, plasma, viridis, purples, oranges, greens are all good ones!
colors = c(ra) 

figure_color = plt.figure(2)
figure_color = subplots_adjust(top=0.96, bottom=0.2, left=0.16, right=0.96)
axes_color = figure_color.add_subplot(111)
axes.plot(
'''
