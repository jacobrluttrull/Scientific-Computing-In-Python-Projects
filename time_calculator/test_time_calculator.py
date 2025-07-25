import unittest
from time_calculator import add_time

class TestAddTime(unittest.TestCase):

    # Provided by FreeCodeCamp
    def test_simple_addition(self):
        self.assertEqual(add_time("3:30 PM", "2:12"), "5:42 PM")

    def test_am_to_pm(self):
        self.assertEqual(add_time("11:55 AM", "3:12"), "3:07 PM")

    def test_next_day(self):
        self.assertEqual(add_time("9:15 PM", "5:30"), "2:45 AM (next day)")

    def test_multiple_days_later(self):
        self.assertEqual(add_time("11:59 PM", "24:05"), "12:04 AM (2 days later)")

    def test_day_of_week_case(self):
        self.assertEqual(add_time("2:59 AM", "24:00", "saturDay"), "2:59 AM, Sunday (next day)")

    def test_long_duration(self):
        self.assertEqual(add_time("8:16 PM", "466:02"), "6:18 AM (20 days later)")

    def test_zero_duration(self):
        self.assertEqual(add_time("3:30 PM", "0:00"), "3:30 PM")

    def test_day_of_week_included(self):
        self.assertEqual(add_time("3:30 PM", "2:12", "Monday"), "5:42 PM, Monday")

    def test_day_rollover_with_day(self):
        self.assertEqual(add_time("11:59 PM", "24:05", "Wednesday"), "12:04 AM, Friday (2 days later)")

    def test_day_of_week_whitespace(self):
        self.assertEqual(add_time("10:00 AM", "48:00", "   SunDAy "), "10:00 AM, Tuesday (2 days later)")

    # ---- Additional Custom Tests ----

    def test_midnight_rollover(self):
        self.assertEqual(add_time("11:59 PM", "0:02"), "12:01 AM (next day)")

    def test_exact_midnight(self):
        self.assertEqual(add_time("12:00 AM", "24:00"), "12:00 AM (next day)")

    def test_midday_edge(self):
        self.assertEqual(add_time("12:00 PM", "12:00"), "12:00 AM (next day)")

    def test_single_minute_add(self):
        self.assertEqual(add_time("1:59 PM", "0:01"), "2:00 PM")

    def test_leading_zero_minutes(self):
        self.assertEqual(add_time("6:01 AM", "0:59"), "7:00 AM")

    def test_full_week_rollover(self):
        self.assertEqual(add_time("5:00 PM", "168:00", "Monday"), "5:00 PM, Monday (7 days later)")

    def test_half_week_rollover(self):
        self.assertEqual(add_time("5:00 PM", "84:00", "Monday"), "5:00 AM, Friday (4 days later)")

    def test_non_integer_hours(self):
        self.assertEqual(add_time("10:15 AM", "0:45"), "11:00 AM")

    def test_noon_to_midnight(self):
        self.assertEqual(add_time("12:00 PM", "12:00"), "12:00 AM (next day)")

    def test_am_pm_flip_on_exact_hour(self):
        self.assertEqual(add_time("11:00 AM", "1:00"), "12:00 PM")

    def test_am_pm_flip_minute_sensitive(self):
        self.assertEqual(add_time("11:59 AM", "0:01"), "12:00 PM")


if __name__ == "__main__":
    unittest.main()
