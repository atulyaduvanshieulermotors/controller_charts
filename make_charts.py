
import ast

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from get_controller_data import get_values
import traceback

ac_comp_speeds = []
ac_comp_currents = []
ac_comp_voltages = []

def update_data(i):
    data = get_values()

    print("Raw Data: ", data)
    
    ac_comp_speed = data[0]
    ac_comp_current = data[1]
    ac_comp_voltage = data[2]

    try:

        if ac_comp_speed != []:
            ax1.cla()
            ax1.set_title("Comp Speed")
            ax1.set_xlabel("Time(sec)")
            ax1.set_ylabel("Comp Speed")
            ax1.set_ylim([-1, 3500])
            
            ac_comp_speeds.append(ac_comp_speed[-1])
            print("AC Comp Speed: ", ac_comp_speed)
            ax1.plot(ac_comp_speeds, color='green')
            ax1.scatter(len(ac_comp_speeds)-1, ac_comp_speeds[-1])
            ax1.text(len(ac_comp_speeds)-1, ac_comp_speeds[-1]+2, "{} rpm".format(ac_comp_speeds[-1]))

        if ac_comp_current != []:
            ax2.cla()
            ax2.set_title("Comp Current")
            ax2.set_xlabel("Time(sec)")
            ax2.set_ylabel("Comp Current")
            ax2.set_ylim([-1, 10])
            
            ac_comp_currents.append(ac_comp_current[-1])
            print("AC Comp Current: ", ac_comp_current)
            ax2.plot(ac_comp_currents, color='green')
            ax2.scatter(len(ac_comp_currents)-1, ac_comp_currents[-1])
            ax2.text(len(ac_comp_currents)-1, ac_comp_currents[-1]+2, "{} A".format(ac_comp_currents[-1]))  

        if ac_comp_voltage != []:
            ax3.cla()
            ax3.set_title("Comp Voltage")
            ax3.set_xlabel("Time(sec)")
            ax3.set_ylabel("Comp Voltage")
            ax3.set_ylim([-1, 160])
            
            ac_comp_voltages.append(ac_comp_voltage[-1])
            print("AC Comp Voltage: ", ac_comp_voltage)
            ax3.plot(ac_comp_voltages, color='green')
            ax3.scatter(len(ac_comp_voltages)-1, ac_comp_voltages[-1])
            ax3.text(len(ac_comp_voltages)-1, ac_comp_voltages[-1]+2, "{} V".format(ac_comp_voltages[-1]))    
			
    except Exception as exc:
        traceback.print_tb(exc)
        print(exc)


fig = plt.figure(figsize=(5, 5), facecolor="#DEDEDE")

ax1 = plt.subplot(2, 2, 1)
ax1.set_facecolor("black")
ax1.set_title("Compressor Speed")
ax1.set_xlabel("Time(sec)")
ax1.set_ylabel("Compressor Speed")
ax1.set_ylim([-1, 5000])

ax2 = plt.subplot(2, 2, 2)
ax2.set_facecolor("black")
ax2.set_title("Compressor Current")
ax2.set_xlabel("Time(sec)")
ax2.set_ylabel("Compressor Current")
ax2.set_ylim([-1, 20])

ax3 = plt.subplot(2, 2, 3)
ax3.set_facecolor("black")
ax3.set_title("Compressor Voltage")
ax3.set_xlabel("Time(sec)")
ax3.set_ylabel("Compressor Voltage")
ax3.set_ylim([-1, 180])


ani = FuncAnimation(fig, update_data, interval=20 )
#ani.save('abc.png')
#ani.show()
plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom= 0.1)
plt.show()
# plt.savefig('abc.png')
