import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def test_correct_name(self):
        worker = Worker("John", 100, 100)
        result = worker.name
        expected = "John"
        self.assertEqual(result, expected)

    def test_correct_increment(self):
        worker1 = Worker("John", 100, 100)
        worker1.rest()
        result = worker1.energy
        expected = 101
        self.assertEqual(result, expected)

    def test_error_raise(self):
        worker1 = Worker("John", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker1.work()
        self.assertEqual("Not enough energy.", ex.exception.args[0])

    def test_error_raise_(self):
        worker1 = Worker("John", 100, -1)
        with self.assertRaises(Exception) as ex:
            worker1.work()
        self.assertEqual("Not enough energy.", ex.exception.args[0])

    def test_salary_increase(self):
        worker1 = Worker("John", 100, 100)
        worker1.work()
        result = worker1.money
        expected = 100
        self.assertEqual(result, expected)

    def test_energy_decrease(self):
        worker1 = Worker("John", 100, 100)
        worker1.work()
        result = worker1.energy
        expected = 99
        self.assertEqual(result, expected)

    def test_get_info(self):
        worker1 = Worker("John", 100, 100)
        result = worker1.get_info()
        expected = 'John has saved 0 money.'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
