import os
import math
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import random
import numpy as np
import csv
import pandas as pd

df=pd.read_csv('unemployment-data-cleaned.csv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
dateCol = df['Year'].tolist()

fpath = os.path.join(rcParams["datapath"], "fonts/ttf/Oswald-VariableFont_wght.ttf")
prop = fm.FontProperties(fname=fpath, weight='bold', size=19)
fname = os.path.split(fpath)[1]

xticks = []
intervals = np.linspace(0, len(dateCol) -1, num=len(dateCol))
xticks = [dateCol[math.floor(interval)] for interval in intervals]

fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(16,9))
# fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

x_locs = np.arange(len(dateCol))
ax.set_xticks(x_locs)
ax.set_xticklabels(dateCol)
ax.set_xlim(0.0, 10)

ax.spines['left'].set_color('#8CD4EF')
ax.spines['bottom'].set_color('#8CD4EF')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis="x", colors="#2064AF", which='major', pad=15)
ax.tick_params(axis="y", colors="#2064AF", which='major', pad=5)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# ax.set_title('This is a special font: {}'.format(fname), fontproperties=prop)
# ax.set_xlabel('Date', fontproperties=prop)
# ax.set_ylabel('Cases')

xdata = []
lines, data = {}, {}
colors = ["#4187C3", "#8CD4EF", "#F49B9B", "#FEE6C0", "m"]
iterdata = df.iteritems()
next(iterdata)
item = 0
for (columnName, columnData) in iterdata:
    # print('Colunm Name : ', item)
    key = "ln"+ str(item)
    lines[key], = plt.plot([], [], colors[item], animated=True, label=columnName)
    data[key] = []
    item+=1

f = np.linspace(0, len(dateCol)+1, len(dateCol)+1)

def init():
    ax.set_ylim(0, 25000)
    return lines["ln0"],

count = 0

legend = plt.legend()
def update(i):
    global count, lines, data, legend, prop
    ax.set_xlim(0.0, len(dateCol))
    xdata.append(i)
    item = 0
    iterdata = df.iteritems()
    print(data['ln0'])

    if(count < len(dateCol) - 1):
        next(iterdata)
        for (columnName, columnData) in iterdata:
            key = "ln" + str(item)
            data[key].append(float(columnData[count]))
            lines[key].set_data(xdata, data[key])
            item+=1

        count+=1
    legend.remove()
    legend = plt.legend(bbox_to_anchor=(1.275, 0.7), frameon=False, prop=prop)
    return lines["ln0"],

for label in ax.get_xticklabels() :
    label.set_fontproperties(prop)
for label in ax.get_yticklabels() :
    label.set_fontproperties(prop)


ani = FuncAnimation(fig, update, frames=f,
                    init_func=init, blit=True, interval=20,repeat=False)
ani.save('animated-chart.mp4')
fig.savefig('transparent-chart.png', transparent=True)
# plt.xlabel('Date')
# plt.ylabel('Cases')
plt.title('Unemployment Data')
# plt.legend(prop=prop)
plt.show()
