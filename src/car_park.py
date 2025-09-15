import json
from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = set(plates or []) #change list to set prevent duplicate plates
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
        if len(self.plates) < self.capacity:
            self.plates.add(plate)
            self.update_displays()
            self._log_car_activity(plate, "entered")
        else:
            print("Car park full! Cannot add car.")

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
            self._log_car_activity(plate, "exited")
        else:
            print(f"Plate {plate} not found in car park.")

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

    def write_config(self):
        with open("config.json", "w") as f:  # TODO: use self.config_file; use Path; add optional parm to __init__
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def save_config(self):
        return CarPark.from_config(config_file=Path("config.json")).write_config()
