import copy
import random
from collections import Counter



class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        trial_hat = copy.deepcopy(hat)

        drawn = trial_hat.draw(num_balls_drawn)
        drawn_counter = Counter(drawn)
        meets = all(drawn_counter.get(color, 0) >= count for color, count in expected_balls.items())
        if meets:
            successes += 1
    return successes / num_experiments

hat = Hat(blue=3, red=2)
print("Initial hat contents:", hat.contents)
print("Draw 2:", hat.draw(2))
print("Remaining hat contents:", hat.contents)
