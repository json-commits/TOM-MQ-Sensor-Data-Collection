import serial.tools.list_ports
import serial



# ports = list(serial.tools.list_ports.comports(include_links=True))
#
# arduino_ports = []
#
# for p in ports:
#     if p.description.startswith("Arduino") or p.description.startswith("USB-SERIAL CH340"):
#         arduino_ports.append(p.device)

arduino_ports = ['COM3', 'COM6', 'COM7', 'COM11']
# arduino_ports = ['COM3']

print(f"Found ports: {arduino_ports}")

open_ports = []
for port in arduino_ports:
    print(f"Opening {port}")
    open_ports.append(serial.Serial(port, 9600))

while True:
    readout = ""
    for port in open_ports:
        # print(f"Readout of {port}")
        readline = port.readline().decode()
        print(readline)
        readout += port.readline().decode()
    print(readout)

    import os
    file_name = "aeration20_12-09-23"  # change this for each testcase

    # make log file if it doesn't exist
    if not os.path.isfile(f"{file_name}.txt"):
        with open("raw_data (12-09-2023)/output.txt", "w") as f:
            f.write("")

    # output readout into a log file called output.txt
    with open(f"{file_name}.txt", "a") as f:
        f.write(readout + "\n")

    readout_list = readout.split("\n")
    time_list = []
    for readout_line in readout_list:
        readout_line = readout_line.split("\t")
        # print(readout_line[0])
        try:
            time_list.append(float(readout_line[0]))
        except ValueError:
            pass
    if min(time_list) > 150:
        break