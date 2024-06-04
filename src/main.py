from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


car_park = CarPark(location="moondalup", capacity=100, log_file='moondalup.txt')
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)
car_park.register(Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park))

entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()

exit_sensor.detect_vehicle()
exit_sensor.detect_vehicle()
