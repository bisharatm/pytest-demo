import src.greeter as greeter
import unittest

class SayHelloTestCase(unittest.TestCase):
    # Test greeter.sayHello()
    # .sayHello() -> Hello, Stranger!
    # .sayHello(name) -> Hello, name!

    def test_sayHello_without_name(self):
        self.assertEqual(greeter.sayHello(), 'Hello, Stranger!')

    def test_sayHello_with_name(self):
        self.assertEqual(greeter.sayHello('John'), 'Hello, John!')