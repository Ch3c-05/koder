import pygame
import math

class Ball():
    def ___init___(self,position,velocity,gravity,static,radius,floor,bounce):
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.gravity = gravity
        self.floor = floor
        self.bounce = bounce
        self.static = static
    
    def update(self):
        if self.static == False:
            self.velocity.y += self.gravity
            self.position += self.velocity

    def check_collision(self,target,targetsize):
        if target.x < self.position.x < target.x + targetsize.x and target.y > self.position.y > target.y - targetsize.y and self.velocity.y > 5:
            return True
        return False
