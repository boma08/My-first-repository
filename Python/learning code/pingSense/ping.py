import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for i in kwargs:
            self.contents.extend([i]*kwargs[i])
    def draw(self,num):
        if num>len(self.contents):
            removed=self.contents.copy()
            self.contents=[]
        else:
            removed=[]
            for i in range(num):
                removing=random.choice(self.contents)
                removed.append(removing)
                self.contents.remove(removing)
        return removed

 
        

def experiment(*, hat, expected_balls, num_balls_drawn, num_experiments):
    success=0
    for i in range(num_experiments):
        drawn=hat.draw(num_balls_drawn)
        correct=True
        for j in expected_balls:
            if expected_balls[j]>drawn.count(j):
                correct=False
        if correct:
            success+=1
        hat.contents.extend(drawn)
    return success/num_experiments



hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=15, black=2, green=13, pink=4, striped=9)

expected_balls_from_draw = {
    "red": 1,
    "green": 2
}

print(experiment(hat=hat3, expected_balls=expected_balls_from_draw, num_balls_drawn=7, num_experiments=20))