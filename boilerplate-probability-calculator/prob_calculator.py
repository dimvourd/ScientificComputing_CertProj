import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, di: dict = None, **kwargs):
        contents = []

        if di is not None:
            for i in di:
                for j in range(di[i]):
                    contents.append(i)
        else:
            for i in kwargs:
                for j in range(kwargs[i]):
                    contents.append(i)

        self.contents = contents

    def draw(self, numb_balls):
        drawn = []
        if numb_balls < len(self.contents):
            for i in range(numb_balls):
                drawn_ball = self.contents[random.randrange(len(self.contents))]
                drawn += [drawn_ball]
                self.contents.remove(drawn_ball)
        else:
            for i in range(len(self.contents)):
                drawn_ball = self.contents[random.randrange(len(self.contents))]
                drawn += [drawn_ball]
                self.contents.remove(drawn_ball)

        return drawn

    def __str__(self):
        return ", ".join(self.contents)


def experiment(hat: Hat, expected_balls, num_balls_drawn: int, num_experiments: int):
    counter = 0
    expected_balls = Hat(expected_balls).contents
    # experiment
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        actual_balls = hat_copy.draw(num_balls_drawn)
        count_same_balls = 0
        for ball in expected_balls:
            if ball in actual_balls:
                actual_balls.remove(ball)
                count_same_balls += 1

        if count_same_balls == len(expected_balls):
            counter += 1

    return counter / num_experiments
