import serial.tools.list_ports
import threading

import serial


ports = list(serial.tools.list_ports.comports(include_links=True))

arduino_ports = []
for p in ports:
    if p.description.startswith("Arduino"):
        arduino_ports.append(p.device)


open_ports = []
for port in arduino_ports:
    open_ports.append(serial.Serial(port, 9600))

# while True:
#     readout = ""
#     for port in open_ports:
#         readout += str(port.readline()) + "\t"
#     print(readout)



import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import tmp102

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with TMP102
# tmp102.init()


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    # Read temperature (Celsius) from TMP102
    temp_c = open_ports[0].readline().decode()

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    # xs = xs[-20:]
    # ys = ys[-20:]

    # set the limits
    ax.set_ylim([200, 800])

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    # plt.subplots_adjust(bottom=0.30)
    # plt.title('TMP102 Temperature over Time')
    # plt.ylabel('Temperature (deg C)')


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
