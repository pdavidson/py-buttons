import unittest
import Stoplight as Stoplight


class TestStoplight(unittest.TestCase):

    def setUp(self):
        self.stoplight = Stoplight('aabbcc')

    def test_push(self):
        self.stoplight.push('a')
        current = self.stoplight.get()
        self.assertEquals(current, 'a')




