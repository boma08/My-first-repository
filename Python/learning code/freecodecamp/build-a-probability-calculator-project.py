import copy
import random

class Hat:
    
    def __init__(self, default_ball=1, **kwargs):
        self.contents_dict = kwargs
        self.contents = []
        for ball in self.contents_dict:
            for _ in range(self.contents_dict[ball]):
                self.contents.append(ball)

    def draw(self, num):
        drawn_balls = []
        if num > len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents = []
        else:
            for _ in range(num):
                random_ball = random.choice(self.contents)
                self.contents.remove(random_ball)
                drawn_balls.append(random_ball)

        return drawn_balls


def experiment(*, hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments
    current_hat = hat.contents.copy()

    while num_experiments >= 1:
        drawn_balls = hat.draw(num_balls_drawn)
        outcome = {
            key: 0 for key in expected_balls
        }

        for draw in drawn_balls:
            for ball in expected_balls:
                if draw == ball:
                    outcome[draw] += 1

        test = []
        for ball in outcome:
            if outcome[ball] >= expected_balls[ball]:
                test.append(True)
            else:
                test.append(False)
        
        if all(test):
            M += 1
                  
        num_experiments -= 1
        hat.contents = current_hat.copy()
    
    return M / N 


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=15, black=2, green=13, pink=4, striped=9)

expected_balls_from_draw = {
    "red": 1,
    "green": 2
}

print(experiment(hat=hat3, expected_balls=expected_balls_from_draw, num_balls_drawn=7, num_experiments=20))
