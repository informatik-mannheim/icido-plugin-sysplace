# ICIDO Plugin for SysPlace
ICIDO Plugin that listens for UDP packets containing a JSON that tells the system
- the *color* and
- the *presence*
of a car. 

Whenever the presence or color changes, the ICIDO system renders either an entering or a leaving car or the color of the car, respectively. The code runs on Python2.7 only.

# Usage and configuration
In order to run the plugin, just use the file `socketGet.py` as an ICIDO Plugin. Be sure to either put `ip` and `port` into `IPConfig.py` or hardcode them into `socketGet.py` (in the one place where those two variables are used).

# JSON format

The JSON format is:

```json
{
  "inside":"true|false",
  "color":"green|blue"
}
```

# Simulator
To use a Commandline simulator, just run 

```Bash
$ python simulator.py
```

To change the simulation, open `simulator.py` and change those lines:

```Python
fakeSocket.enqueue(Packet("blue", False))
fakeSocket.enqueue(Packet("blue", False))
fakeSocket.enqueue(Packet("green", False))
fakeSocket.enqueue(Packet("green", True))
fakeSocket.enqueue(Packet("green", True))
fakeSocket.enqueue(Packet("blue", True))
# [...]
```

Packets will be "sent" to the server in the exact order they are enqueued. The Server behavior will be printed to the command line.

# Tests
There are some unit tests that can be run:

```Shell
$ python tests.py
```

By setting the verbose flag with `setVerbose(True|False)`, the test output can be adjusted.
