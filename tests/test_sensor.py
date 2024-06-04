import unittest
from sensor import Sensor, ExitSensor, EntrySensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.sensor = Sensor(1, self.car_park)

    def test_display_initialized_with_all_attributes(self):
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, False)
        self.assertIsInstance(self.sensor.car_park, CarPark)


class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.car_park.add_car('FAKE-123')
        self.sensor = EntrySensor(1, self.car_park)

    def test_update_car_park_add_car(self):
        self.sensor.update_car_park('FAKE-111')
        self.assertIn('FAKE-111', self.car_park.plates)


class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 99)
        self.car_park.add_car('FAKE-222')
        self.sensor = ExitSensor(1, self.car_park)

    def test_update_car_park_remove_car(self):
        self.sensor.update_car_park('FAKE-222')
        self.assertNotIn('FAKE-222', self.car_park.plates)


if __name__ == '__main__':
    unittest.main()
