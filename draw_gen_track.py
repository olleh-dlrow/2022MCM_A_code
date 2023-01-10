from matplotlib import pyplot as plt
import pandas as pd

save_dir = './GenTrack/'
altitude_file = 'gen_track.csv'
res_file = 'gen_track_save.csv'

img_name = ['speed', 'w', 'u', 'Umax', 'Umode']
img_name = [save_dir + name + '.png' for name in img_name]

# 读海拔图 AltitudeMeters DistanceMeters
altitude = pd.read_csv(altitude_file)
fig, ax = plt.subplots()

ax.plot(altitude['DistanceMeters'], altitude['AltitudeMeters'])
ax.grid(True)
ax.set_xlabel('distance(m)')
ax.set_ylabel('altitude(m)')
ax.set_title('Altitude Curse')
fig.savefig(save_dir + 'altitude.png')

# distance,speed,w,u,Umax,Umode,Time
data = pd.read_csv(res_file)

fig, ax = plt.subplots()

ax.plot(data['distance'], data['speed'])
ax.grid(True)
ax.set_xlabel('distance(m)')
ax.set_ylabel('speed(m/s)')
ax.set_title('Speed Curse')
fig.savefig(img_name[0])

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('distance(m)')
ax.set_ylabel('remaining anaerobic energy(J)')
ax.set_title('Remaining Anaerobic Energy Curse')
ax.plot(data['distance'], data['w'])
fig.savefig(img_name[1])

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('distance(m)')
ax.set_ylabel('power(Watts)')
ax.set_title('Power Curse')
ax.plot(data['distance'], data['u'])
fig.savefig(img_name[2])

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('distance(m)')
ax.set_ylabel('max power(Watts)')
ax.set_title('Max Power Curse')
ax.plot(data['distance'], data['Umax'])
fig.savefig(img_name[3])

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('distance(m)')
ax.set_ylabel('power mode')
ax.set_title('Power Mode Use')
ax.plot(data['distance'], data['Umode'], 'x', 'markersize', 0.4)
fig.savefig(img_name[4])


