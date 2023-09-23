from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(
            20.5, 175.5
        )

    def test_default_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_not_enough_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_enough_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(18, self.vehicle.fuel)

    def test_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_successfully_refueled(self):
        self.vehicle.fuel -= 1
        self.vehicle.refuel(1)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test_correct__str__(self):
        result = str(self.vehicle)
        expected = f"The vehicle has 175.5 " \
                   f"horse power with 20.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
