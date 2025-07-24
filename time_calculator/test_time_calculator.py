import unittest
from time_calculator import add_time

class TestAddTime(unittest.TestCase):
    def test_basic_addition(self):
        self.assertEqual(add_time('3:30 PM', '2:12'), '5:42 PM')
        self.assertEqual(add_time('11:55 AM', '3:12'), '3:07 PM')
        self.assertEqual(add_time('2:59 AM', '24:00'), '2:59 AM (next day)')
        self.assertEqual(add_time('11:59 PM', '24:05'), '12:04 AM (2 days later)')
        self.assertEqual(add_time('8:16 PM', '466:02'), '6:18 AM (20 days later)')
        self.assertEqual(add_time('3:30 PM', '0:00'), '3:30 PM')

    def test_with_day(self):
        self.assertEqual(add_time('3:30 PM', '2:12', 'Monday'), '5:42 PM, Monday')
        self.assertEqual(add_time('2:59 AM', '24:00', 'saturDay'), '2:59 AM, Sunday (next day)')
        self.assertEqual(add_time('11:59 PM', '24:05', 'Wednesday'), '12:04 AM, Friday (2 days later)')
        self.assertEqual(add_time('8:16 PM', '466:02', 'tuesday'), '6:18 AM, Monday (20 days later)')

    def test_period_boundary(self):
        self.assertEqual(add_time('11:59 AM', '0:01'), '12:00 PM')  # AM to PM transition
        self.assertEqual(add_time('11:59 PM', '0:01'), '12:00 AM (next day)')  # PM to AM + next day

if __name__ == '__main__':
    unittest.main()
