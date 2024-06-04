from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        location = self.location
        capacity = self.capacity
        return f"Welcome to {location}, there are {capacity} left"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        data = {"available_bays": self.available_bays, "Temperature": 25}
        for display in self.displays:
            display.update(data)
            print(f"Updated {display}")

    @property  # return any method into property
    def available_bays(self):
        # car_park.available_bays
        return max(0, self.capacity - len(self.plates))

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action}\n")

