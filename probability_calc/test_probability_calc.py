# test_probability_calc.py
import unittest
from collections import Counter
from probability_calc.probability_calc import Hat, experiment


class TestHat(unittest.TestCase):

    def test_creation_builds_correct_contents(self):
        hat = Hat(blue=2, red=1, green=0)
        self.assertEqual(Counter(hat.contents), Counter({"blue": 2, "red": 1}))
        # Ensure exact items present (no extras like 'green')
        self.assertEqual(sorted(hat.contents), ["blue", "blue", "red"])

    def test_draw_reduces_contents(self):
        hat = Hat(red=3, blue=2)
        start_len = len(hat.contents)
        drawn = hat.draw(3)
        self.assertEqual(len(drawn), 3)
        self.assertEqual(len(hat.contents), start_len - 3)
        # Ensure drawn balls came from the hat
        self.assertTrue(Counter(drawn) <= Counter(["red"] * 3 + ["blue"] * 2))

    def test_draw_more_than_available_returns_all(self):
        hat = Hat(red=2, blue=1)
        total = len(hat.contents)
        drawn = hat.draw(10)  # more than available
        self.assertEqual(len(drawn), total)
        self.assertEqual(hat.contents, [])  # hat should be empty

    def test_experiment_returns_probability_between_0_and_1(self):
        # Choose a setup where probability is strictly between 0 and 1
        hat = Hat(blue=5, red=4, green=2)
        p = experiment(
            hat=hat,
            expected_balls={"red": 1, "green": 1},
            num_balls_drawn=4,
            num_experiments=1500
        )
        self.assertIsInstance(p, float)
        self.assertGreater(p, 0.0)
        self.assertLess(p, 1.0)
        # Run again: probability may differ since it's random
        q = experiment(
            hat=Hat(blue=5, red=4, green=2),
            expected_balls={"red": 1, "green": 1},
            num_balls_drawn=4,
            num_experiments=1500
        )
        # Optional: skip strict inequality to avoid flaky test
        # self.assertNotEqual(p, q)


if __name__ == "__main__":
    unittest.main()
