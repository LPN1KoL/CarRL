import math
import pygame


acceleration = 1
speed_limit = 30


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.L = 30
        self.steering = 0
        self.next_checkpoint = 0
        self.image = self.draw()


    def forward(self):
        if 0 <= self.speed <= speed_limit - acceleration:
            self.speed += acceleration
        elif self.speed < 0:
            self.speed += acceleration * 2


    def backward(self):
        if 0 >= self.speed >= -speed_limit + acceleration:
            self.speed -= acceleration
        elif self.speed > 0:
            self.speed -= acceleration * 2


    def stop(self):
        if -speed_limit <= self.speed < 0:
            self.speed += acceleration
        elif 0 < self.speed <= speed_limit:
            self.speed -= acceleration


    def move(self):
        angle_rad = math.radians(self.angle)
        self.x += self.speed/3 * math.cos(angle_rad)
        self.y -= self.speed/3 * math.sin(angle_rad)


    def turn_right(self):
        if self.speed > 5:
            self.angle -= 5
            self.steering = 30
        elif self.speed < -5:
            self.angle += 5
            self.steering = -30


    def turn_left(self):
        if self.speed > 5:
            self.angle += 5
            self.steering = -30
        elif self.speed < -5:
            self.angle -= 5
            self.steering = -30


    def display(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)


    @staticmethod
    def draw():
        car_image = pygame.Surface((40, 20), pygame.SRCALPHA)
        car_image.fill((200, 50, 50))
        pygame.draw.rect(car_image, (100, 180, 220), (25, 3, 10, 14))
        pygame.draw.rect(car_image, (100, 25, 25), (0, 0, 6, 20))
        pygame.draw.rect(car_image, (200, 200, 100), (37, 2, 3, 5))
        pygame.draw.rect(car_image, (200, 200, 100), (37, 13, 3, 5))
        return car_image

