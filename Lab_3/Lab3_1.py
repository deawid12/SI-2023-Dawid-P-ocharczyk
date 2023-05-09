import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

year = np.array([2000, 2002, 2005, 2007, 2010])
procent_reg = np.array([6.5, 7.0, 7.4, 8.2, 9.0])


slope, intercept = np.polyfit(year, procent_reg, 1)
print(f"Model regresji liniowej: y = {slope:.3f}x + {intercept:.3f}")


target_percentage = 12.0
target_year = (target_percentage - intercept) / slope
print(f"Procent bezrobotnych przekroczy 12% w {target_year:.0f}")

lata = np.append(year, target_year)
prc = np.append(procent_reg, target_percentage)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
scat = ax.scatter([], [])

def init():
    ax.set_xlim(year[0]-1, target_year+1)
    ax.set_ylim(0, max(procent_reg) + 3.5)
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage')
    ax.set_title('Percentage of Unemployed People')
    return line,

def update(frame):
    xdata = lata[:frame+1]
    ydata = prc[:frame+1]
    scat.set_offsets(np.c_[xdata, ydata])
    if len(xdata) > 1:
        slope, intercept = np.polyfit(xdata, ydata, 1)
        line.set_data(xdata, slope * xdata + intercept)
    return line, scat

animacja = FuncAnimation(fig, update, frames=len(lata), init_func=init, blit=True)
plt.show()
