class Sensor:
    def __init__(self, id, car_park, is_active=False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

        def __str__(self):
            return f'{self.id}: Sensor is {"is active" if self.is_active else "if active"}'

    class EntrySensor(Sensor):
        pass
    class ExitSensor(Sensor):
        pass
