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

        if check_collision(screen, car):
            break

        checkpoint(screen, car)

        car.display(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


def check_collision(scrn, car):
    track_image = pygame.image.load("maps/map1.png").convert()
    wall_mask = pygame.mask.from_threshold(track_image, (255, 127, 39), (5, 5, 5, 255))
    rotated_image = pygame.transform.rotate(car.image, car.angle)
    car_mask = pygame.mask.from_surface(rotated_image)

    scrn.blit(track_image, (0, 0))

    rect = rotated_image.get_rect(center=(car.x, car.y))
    offset = (rect.left - 0, rect.top - 0)
    collision_point = wall_mask.overlap(car_mask, offset)

    if collision_point is not None:
        time.sleep(0.5)
        return True
    return False


def create_checkpoint(scrn):
    checkpoints = [
        pygame.Surface((10, 230), pygame.SRCALPHA),
        pygame.Surface((10, 230), pygame.SRCALPHA),
        pygame.Surface((10, 230), pygame.SRCALPHA),
        pygame.Surface((200, 10), pygame.SRCALPHA),
        pygame.Surface((10, 170), pygame.SRCALPHA),
        pygame.Surface((10, 130), pygame.SRCALPHA),
        pygame.Surface((200, 10), pygame.SRCALPHA),
    ]

    for cp in checkpoints:
        cp.fill((80, 80, 80))

    checkpoints_placement = [
        scrn.blit(checkpoints[0], (300, 20)),
        scrn.blit(checkpoints[1], (600, 20)),
        scrn.blit(checkpoints[2], (1000, 20)),
        scrn.blit(checkpoints[3], (1180, 300)),
        scrn.blit(checkpoints[4], (600, 300)),
        scrn.blit(checkpoints[5], (1000, 520)),
        scrn.blit(checkpoints[6], (30, 500))
    ]

    return checkpoints, checkpoints_placement


def checkpoint(scrn, car):
    checkpoints, checkpoints_placement = create_checkpoint(scrn)
    checkpoint_mask = pygame.mask.from_surface(checkpoints[car.next_checkpoint])
    rotated_image = pygame.transform.rotate(car.image, car.angle)
    car_mask = pygame.mask.from_surface(rotated_image)

    rect = rotated_image.get_rect(center=(car.x, car.y))
    cp_offset = (rect.left - checkpoints_placement[car.next_checkpoint].left, rect.top - checkpoints_placement[car.next_checkpoint].top)
    checkpoint_touch = checkpoint_mask.overlap(car_mask, cp_offset)

    if checkpoint_touch is not None:
        print("Checkpoint!")
        car.next_checkpoint += 1 if car.next_checkpoint < len(checkpoints)-1 else -len(checkpoints)+1


if __name__ == "__main__":
    run()
