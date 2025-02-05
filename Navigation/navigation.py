from Navigation.directions import Steering, Motor
import random

class Navigation():

    def random_move():
        rand_steering  = random.randint(1,3)
        rand_motor  = random.randint(1,3)

        move = [None, None]

        if rand_steering == 1:
            move[0] = Steering.LEFT
        if rand_steering == 2:
            move[0] = Steering.RIGHT
        if rand_motor == 1:
            move[1] = Motor.FORWARD
        if rand_motor == 2:
            move[1] = Motor.BACKWARD
        
        move = (move[0], move[1])

        return move

        