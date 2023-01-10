from cProfile import label
from matplotlib import pyplot as plt
import pandas as pd

save_dir = './Tokyo/'
TT_power_file = 'Tokyo_save.csv'
Sprinter_power_file = 'Tokyo_save_Sprinter.csv'

altitude_file = 'Tokyo.csv'

al_data = pd.read_csv(altitude_file)
altitudes = al_data['AltitudeMeters']

img_file = save_dir + 'ComparePower_Tokyo.png'

TT_data, Sprinter_data = pd.read_csv(TT_power_file), pd.read_csv(Sprinter_power_file)
TT_power, Sprinter_power = TT_data['u'], Sprinter_data['u']

fig, ax = plt.subplots()
x = TT_data['distance']

color = 'tab:blue'
ax.plot(x, TT_power, '-', label='Time Trial Specialist')
ax.plot(x, Sprinter_power, '--', label='Sprinter')
ax.legend()
ax.set_xlabel('distance(m)')
ax.set_ylabel('power(Watts)', color=color)
ax.set_title('Power Comparison of Riders')
ax.tick_params(axis='y', labelcolor=color)

ax2 = ax.twinx()
color = 'tab:green'
ax2.set_ylabel('altitude(m)', color=color)  # we already handled the x-label with ax1
ax2.fill_between(al_data['DistanceMeters'], min(altitudes), altitudes, facecolor=color, alpha=0.1)
ax2.tick_params(axis='y', labelcolor=color)

fig.savefig(img_file)
