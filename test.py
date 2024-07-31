import pygame as pg

pg.init()
screen = pg.display.set_mode((1300, 800))
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Draw circles
    screen.fill((0, 0, 0))  # Clear screen
    for x in range(50, 1300, 80):
        for y in range(300, 0, -80):
            pg.draw.circle(screen, (255, 255, 255), (x, y), 25.0)

    pg.display.flip()
    clock.tick(60)

pg.quit()