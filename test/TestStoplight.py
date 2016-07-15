import unittest

from src.Stoplight import Stoplight


class TestStoplight(unittest.TestCase):

    def setUp(self):
        self.stoplight = Stoplight('aabbcc')

    def test_push(self):
        self.stoplight.push('a')
        current = self.stoplight.get()

        self.assertEquals(current, 'a')

    def test_get(self):
        self.stoplight.push('a')
        current = self.stoplight.get()

        self.assertEquals(current, 'a')

    def test_validate_true(self):
        self.stoplight.push('a')
        self.stoplight.push('a')
        self.stoplight.push('b')
        self.stoplight.push('b')
        self.stoplight.push('c')
        self.stoplight.push('c')

        self.assertTrue(self.stoplight.validate())

    def test_validate_false(self):
        self.stoplight.push('a')
        self.stoplight.push('a')
        self.stoplight.push('b')

        self.assertFalse(self.stoplight.validate())

    def test_reset(self):
        self.stoplight.push('a')
        self.stoplight.push('b')
        self.stoplight.reset()

        self.assertEquals(self.stoplight.get(), '')

