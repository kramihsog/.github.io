import pygame
import asyncio


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


async def main():
    x = 320
    speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x += speed
        if x > 600 or x < 0:
            speed = -speed

        screen.fill((30, 30, 30)) 
        pygame.draw.rect(screen, (255, 0, 0), (x, 220, 40, 40)) 

        pygame.display.flip()
        clock.tick(60)
        
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
