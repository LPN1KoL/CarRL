import pygame
from movement import Car

pygame.init()


screen = pygame.display.set_mode((1380, 820))
pygame.display.set_caption("Need for Speed")
clock = pygame.time.Clock()


def run():
    running = True
    car = Car(100, 100)
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

        car.display(screen, car_image)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    run()
