from turtle import speed
from matplotlib import pyplot as plt
import pandas as pd
from scipy import interpolate as intp
import numpy as np


save_dir = './wind/'
speed_file = 'wind_speed_save_modified.csv'
degree_file = 'wind_degree_save.csv'


speed_data = pd.read_csv(speed_file)
x = speed_data['speed']
y = speed_data['time']
f1 = intp.interp1d(x, y, kind = 'cubic')

x_new = np.linspace(min(x), max(x), 100)

fig, ax = plt.subplots()
ax.plot(x_new, f1(x_new), '-', x, y, 'x')
ax.grid(True)
ax.set_xlabel('wind speed(m/s)')
ax.set_ylabel('minimum time(s)')
ax.set_title('Minumum Time On 1km Flat Track(Cubic Interpolate)')
fig.savefig(save_dir + 'speed.png')


# distance,speed,w,u,Umax,Umode,Time
data = pd.read_csv(degree_file)

x = data['degree'] * 180 / np.pi
y = data['time']
f2 = intp.interp1d(x, y, kind = 'cubic')

x_new = np.linspace(min(x), max(x), 100)

fig, ax = plt.subplots()
ax.plot(x_new, f2(x_new), '-', x, y, 'x')
ax.grid(True)
ax.set_xlabel('angle(degree)')
ax.set_ylabel('minimum time(s)')
ax.set_title('Minumum Time On 1km Flat Track(Cubic Interpolate)')
fig.savefig(save_dir + 'degree.png')

