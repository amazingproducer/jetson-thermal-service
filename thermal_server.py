#!/bin/env python3

import socketserver

SERVER_HOST = "0.0.0.0" # String, address of service host 
SERVER_PORT = None # Integer, listening port for service

class ThermalRequestHandler(socketserver.BaseRequestHandler):
    """
    Returns thermal sensor readings from host to UDP client.
    """
    def get_temp_result(self, zone, ztype="Average"):
        """
        Accepts thermal zone ID and Type as parameters, returns formatted temperature result.
        If no ztype is named, returns result from weighted average (thermal zone 5).
        """
        if ztype == "Average":
            zone = 5
        thermal_reading = None
        with open(f'/sys/class/thermal/thermal_zone{zone}/temp') as therm_val:
            thermal_reading = "{:3.2f}".format(float(therm_val.read())/1000)
            result = bytes(f"{ztype}: {thermal_reading}\n", encoding='utf-8')
        return result

    def handle(self):
        """
        Handles requests containing thermal zone types from UDP client and returns
        corresponding thermal readings.
        """
        data_raw, socket = self.request
        temp_result = None
        if data_raw.strip().lower() == b"CPU".lower():
            # get the cpu temp, thermal-zone1
            temp_result = self.get_temp_result(1, "CPU")
        elif data_raw.strip().lower() == b"GPU".lower():
            # get the gpu temp, thermal_zone2
            temp_result = self.get_temp_result(2, "GPU")
        else: # get the average temp, thermal_zone5
            temp_result = self.get_temp_result(5)
        socket.sendto(temp_result, self.client_address)

if __name__ == "__main__":
    HOST, PORT = SERVER_HOST, SERVER_PORT
    with socketserver.UDPServer((HOST, PORT), ThermalRequestHandler) as server:
        server.serve_forever()
