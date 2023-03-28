import time
import pygame

def main():

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((600, 600))

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.

    character = pygame.image.load("char.png")

    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()

    x = 0
    y = 0

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.process_time()
            frame_rate = 500 / (t1-t0)
            t0 = t1

        main_surface.fill((184, 184, 184))

        main_surface.blit(character,(x+5, y+5))

        the_text = my_font.render("{1:.2f} fps".format(frame_count, frame_rate), True, (50, 50, 50))

        main_surface.blit(the_text, (10, 584))

        pygame.display.flip()




    pygame.quit()
main()