from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

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
#        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
#        self.update_displays()

    @property  # return any method into property
    def available_bays(self):
        # car_park.available_bays
        return max(0, self.capacity - len(self.plates))
