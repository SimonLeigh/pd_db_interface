#
#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from power server...")
socket.connect("tcp://192.168.1.113:5556")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

socket.setsockopt(zmq.SUBSCRIBE, "")

# Process 5 updates
while True:
    string = socket.recv_string()
    time, active, apparent, voltage = string.split()

    print("time: %.2f, active: %.2f, apparent: %.2f, voltage: %.2f" % (
        float(time), float(active), float(apparent), float(voltage))
    )
