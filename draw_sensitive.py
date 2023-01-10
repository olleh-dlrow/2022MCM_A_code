from turtle import speed
from matplotlib import pyplot as plt
import pandas as pd
from scipy import interpolate as intp
import numpy as np
import math

save_dir = './sensitive/'
sen_file = '1km_sen.csv'

data = pd.read_csv(sen_file)

labels = [1, 0.9, 0.8, 0.7, 0.6]
labels = [str(label) + 'U' for label in labels]
flat_val = data[0:len(labels)]['time'].values
ramp_val = data[len(labels):len(labels) * 2]['time'].values

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, flat_val, width, label='Flat')
rects2 = ax.bar(x + width/2, ramp_val, width, label='Ramp')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('minimum time(s)')
ax.set_xlabel('power(Watts)')
ax.set_title('Minimum Time Comparison of Different Power in 2 Terrains')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

flat_inc = data[0:len(labels)]['increase'].values
ramp_inc = data[len(labels):len(labels) * 2]['increase'].values

flat_inc = [str(round(val * 100, 2)) + '%' for val in flat_inc]
ramp_inc = [str(round(val * 100, 2)) + '%' for val in ramp_inc]

def autolabel(rects, inc):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect, val in zip(rects, inc):
        height = rect.get_height()
        ax.annotate(val,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1, flat_inc)
autolabel(rects2, ramp_inc)

fig.tight_layout()
fig.savefig(save_dir + 'sensitive.eps', dpi=600)