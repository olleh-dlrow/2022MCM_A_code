from cProfile import label
from matplotlib import pyplot as plt
import pandas as pd

save_dir = './UCI/'
TT_speed_file = 'UCI_save.csv'
Sprinter_speed_file = 'UCI_save_Sprinter.csv'

altitude_file = 'UCI_grad.csv'

al_data = pd.read_csv(altitude_file)
altitudes = al_data['AltitudeMeters']

img_file = save_dir + 'CompareSpeed_UCI.png'

TT_data, Sprinter_data = pd.read_csv(TT_speed_file), pd.read_csv(Sprinter_speed_file)
TT_speed, Sprinter_speed = TT_data['speed'], Sprinter_data['speed']

fig, ax = plt.subplots()
x = TT_data['distance']

color = 'tab:blue'
ax.plot(x, TT_speed, '-', label='Time Trial Specialist')
ax.plot(x, Sprinter_speed, '--', label='Sprinter')
ax.legend()
ax.set_xlabel('distance(m)')
ax.set_ylabel('speed(m/s)', color=color)
ax.set_title('Speed Comparison of Riders')
ax.tick_params(axis='y', labelcolor=color)

ax2 = ax.twinx()
color = 'tab:green'
ax2.set_ylabel('altitude(m)', color=color)  # we already handled the x-label with ax1
ax2.fill_between(al_data['DistanceMeters'], min(altitudes), altitudes, facecolor=color, alpha=0.1)
ax2.tick_params(axis='y', labelcolor=color)

fig.savefig(img_file)
