import subprocess
import os

# This version of the script is optimized for Linux terminals only
# (made in Ubuntu 20.04 LTS)

# (optional) clears everything when the script is run in terminal
def clear():
    os.system('clear')

clear()

# irrelevant text
print("")
print("Python Network Listener (PNL)".center(50, "-"))
print("")

print("Please enter an ip address and name of device:")
print("Examples".center(50, "-"))
print("192.168.0.56 Jim")
print("10.11.0.3 Orla")
print("".center(50, "-"))
# end of irrelevant text

# lets you input the ip from within the program.
ip_input = input(">>> ")
# alternatively add the ip and name into the if statement below

# make sure to only write the ip and name with maximum one space
# between the two.

# this is only for ease of use when testing things out
if ip_input == "1":
    ip_input = "ip_address1 device_name1"
elif ip_input == "2":
    ip_input = "ip_address2 device_name2"

# an array called names which stores the ip and name from ip_input
# hence it is important to write the ip first and then the name
# with a mandatory space between ip and name
names = [
    ip_input.split()[0], ip_input.split()[1]
]

# this line pings the ip you entered in the background thanks to subproccess
output = subprocess.Popen(["ping", names[0]],stdout=subprocess.PIPE)

# this function is where the real magic begins
def scan():
    while True:
        # stores the resolution of the ping in line
        line = output.stdout.readline()

        # this tests wether line is empty, if it isn't the code continues
        if not line:
            print("line empty")
            break

        # here we store the ip from the terminal output *¹
        connected_ip = line.decode('utf-8').split()[3]

        # here we check for a successful ping and print accordingly
        if connected_ip == names[0] + ":":
            # do stuff if device is connected to network
            print(f"{names[1]} is connected")
        else:
            # do stuff if device is not connected to network
            print(f"{names[1]} is not connected")

scan()

# this line will never be printed because of the while loop in scan() *²
print("done")

# -----------------------------------------------------------------------------
# Further Documentation

# *¹
# If the ping is successful the ip of your chosen device should be in the
# specified array location of the line.decode.split() (namely 4th).
# Hence why we use the ip for comparison
#
# Is the ping not successful, either due to an incorrect input of the ip or
# due to the device you're pinging not being connected to the network,
# the line.decode.split()[3] will not equal the entered ip and you will
# receive the message "names[1] is not connected"

# *²
# For now the script is meant to be started when you wish to execute
# some code when a certain device connects to the network, meaning that it
# has to be stopped manually (Ctrl-c in terminal), via the if statement 
# in line 63 by breaking the while loop or by exit()/quit().
# -----------------------------------------------------------------------------
