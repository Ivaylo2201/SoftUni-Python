import unittest


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Cat")

    def test_initialization(self):
        self.assertEqual("Cat", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(0, self.cat.size)

    def test_cat_size_incrementation(self):
        self.cat.eat()
        result = self.cat.size
        expected = 1
        self.assertEqual(result, expected)

    def test_cat_is_fed(self):
        cat = Cat("Cat")
        cat.eat()
        result = cat.fed
        self.assertTrue(result)

    def test_error_cannot_eat(self):
        cat = Cat("Cat")
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_error_cannot_sleep(self):
        cat = Cat("Cat")
        with self.assertRaises(Exception) as ex:
            cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy(self):
        cat = Cat("Cat")
        cat.eat()
        cat.sleep()
        result = cat.sleepy
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
