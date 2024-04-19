import matplotlib.pyplot as plt
from matplotlib import cm

def contourplot_KS(uu):
    # Make contour plot of solution
    fig, ax = plt.subplots()
    ax.contourf(uu, 61, cmap=cm.RdBu, vmin=-2.5, vmax=2.5)
    ax.axis('off')
    plt.show()

