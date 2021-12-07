# jetson-thermal-service: Nano

UDP service to query the state of various thermal sensors on an Nvidia Jetson Nano.

## Included in this Repository:
- `thermal_server.py`: The UDP server application, which should be run from the Jetson Nano device.
- `nanotemp.py`: The UDP client application, which may be run from remote shells capable of reaching the server.
- `jetson-thermal.service`: Basic systemd service unit for integrating the server application with its host OS.

## Client Usage:
```
usage: nanotemp.py [-h] server port [sensor]

positional arguments:
  server      Address of service host.
  port        Listening port of service host.
  sensor      Query a specific thermal sensor (GPU/CPU, optional).

optional arguments:
  -h, --help  show this help message and exit
  ```