import serial
from pythonosc import udp_client

serialport = "/dev/cu.usbmodem143402"

ser = serial.Serial(serialport, 115200)




"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def write_pred_serial(unused_addr, arg1, arg2,arg3):
    print(arg1,arg2,arg3)
    ser.flush()
    if arg1<arg2 and arg1<arg3: 
        ser.write(b"0:")
    elif arg2<arg3 and arg2<arg1:
        ser.write(b"1:")
    else:
        ser.write(b"2:")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=12000, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/wek/outputs",write_pred_serial)


  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()