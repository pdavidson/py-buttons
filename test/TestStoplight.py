import unittest
import Stoplight

class TestStoplight(unittest.TestCase):

    def before(self):
        self.stoplight = Stoplight('aabbcc')

    def test_push(self):
        self.stoplight.push('a')
        current = self.stoplight.get()
        self.assertEquals(current, 'a')




