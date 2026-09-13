acceleration = 1

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0

    def forward(self):
        if self.speed <= 10 - acceleration:
            self.speed += acceleration
        self.x += 1 * self.speed
        return self.x, self.y

    def backward(self):
        if self.speed >= -10 + acceleration:
            self.speed -= acceleration
        self.x += 1 * self.speed
        return self.x, self.y

    def stop(self):
        if -10 <= self.speed < 0:
            self.speed += acceleration
        elif 0 < self.speed <= 10:
            self.speed -= acceleration
        self.x += 1 * self.speed
        return self.x, self.y
