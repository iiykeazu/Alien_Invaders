import sys
import pygame as pg

def check_keydown_events(event, ship):
    """Respond to keypresses."""
    # Move the ship to the left or right.
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Respond to keypresses and mouse evens."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)



def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen. """
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pg.display.flip()
