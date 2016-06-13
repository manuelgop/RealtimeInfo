


import threading
import Adafruit_BMP.BMP085 as BMP085




class SensorThing(object):
    """Internet 'thing' that can control GPIO on a Raspberry Pi."""

    def __init__(self):
        """Initialize the 'thing'."""
        # Setup GPIO library.
        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()

    def read_temp(self):
        """Read the switch state and return its current value.
        """
        with self._lock:
        	sensor = BMP085.BMP085()
        	return sensor.read_temperature()


   