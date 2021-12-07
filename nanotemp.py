#!/bin/env python3

# nanotemp.py - UDP client application to obtain thermal sensor information for a Jetson Nano.

import socket
import sys
import argparse

parser = argparse.ArgumentParser(description='Request temperature readings from remote Jetson Nano sensors.')
parser.add_argument("server", help="Address of service host.")
parser.add_argument("port", help="Listening port of service host.", type=int)
parser.add_argument("sensor", help="Query a specific thermal sensor (GPU/CPU, optional).", nargs='?')#, choices=["GPU", "CPU", None])
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(f"{args.sensor}\n", encoding='utf-8'), (args.server, args.port))
resp = str(sock.recv(1024), encoding='utf-8')
print(resp)