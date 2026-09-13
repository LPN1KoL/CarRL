import math
import pygame
from movement import Car

pygame.init()


screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Need for Speed")
clock = pygame.time.Clock()


def run():
    running = True
    car = Car(100, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((50, 50, 50))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            car.angle -= 5
        if keys[pygame.K_d]:
            car.angle += 5
        if keys[pygame.K_w]:
            car.forward()
        if keys[pygame.K_s]:
            car.backward()
        if not any([keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d]]):
            car.stop()


        car_image = pygame.Surface((40, 20), pygame.SRCALPHA)
        car_image.fill((200, 50, 50))
        rotated = pygame.transform.rotate(car_image, car.angle)
        rect = rotated.get_rect(center=(car.x, car.y))
        screen.blit(rotated, rect)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run()
