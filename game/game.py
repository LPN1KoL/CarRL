import time
import pygame
from movement import Car

pygame.init()


screen = pygame.display.set_mode((1380, 820))
pygame.display.set_caption("Need for Speed")
clock = pygame.time.Clock()


def run():
    running = True
    car = Car(200, 100)
    car_image = car.draw

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((50, 50, 50))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            car.turn_left()
        if keys[pygame.K_d]:
            car.turn_right()
        if keys[pygame.K_w]:
            car.forward()
        elif keys[pygame.K_s]:
            car.backward()
        else:
            car.stop()
        car.move()

        if check_collision(screen, car, car_image):
            break

        car.display(screen, car_image)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


def check_collision(_screen, car, car_image):
    track_image = pygame.image.load("maps/map1.png").convert()
    wall_mask = pygame.mask.from_threshold(track_image, (255, 127, 39), (5, 5, 5, 255))
    rotated_image = pygame.transform.rotate(car_image, car.angle)
    car_mask = pygame.mask.from_surface(rotated_image)

    rect = rotated_image.get_rect(center=(car.x, car.y))
    offset = (rect.left - 0, rect.top - 0)
    collision_point = wall_mask.overlap(car_mask, offset)

    if collision_point is not None:
        time.sleep(0.5)
        return True

    _screen.blit(track_image, (0, 0))
    return False


if __name__ == "__main__":
    run()
