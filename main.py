import game
import time

# Create a Spaceship
spaceship = game.create_shape(0, -220, "basket.gif")

# Create an Asteroid
asteroid = game.create_shape(0, 270, "1.gif")

# Move the spaceship to the left
game.move_left(spaceship, 10)

# Move the spaceship to the right
game.move_right(spaceship, 10)


# Note:game_loop function will be called automatically
def game_loop():
    #game_title("Space Shooter")

    # Move the asteroid downwards and experiment with the speed
    game.move_down(asteroid, 3)

    # Reset the asteroid
    game.reset(asteroid)

    # Track the asteroid
    asteroid_is_close = game.track_asteroid(spaceship, asteroid)

    # Dodge the asteroid
    if asteroid_is_close:
        game.hide(asteroid)
        #dodge_asteroid(spaceship, asteroid)
    time.sleep(0.01)
