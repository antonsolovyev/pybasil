import math
import arcade

# Screen dimension constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
TITLE ='Binary star system'

# Physics constants
M1 = 1
M2 = 25
G = 1e4
TICK_STEPS = 500

# Variables
x1 = SCREEN_WIDTH * 5 / 6
y1 = SCREEN_HEIGHT / 2

x2 = SCREEN_WIDTH * 2 / 6
y2 = SCREEN_HEIGHT / 2

vx1 = 0
vy1 = 15

vx2 = 0
vy2 = - vy1 * M1 / M2 # Ensure center mass has 0 initial velocity

def draw(time_delta):
    arcade.start_render()
    global x1, x2, y1, y2, vx1, vx2, vy1, vy2
    time_step = 1 / TICK_STEPS
    for i in range(0, TICK_STEPS):
        x12 = x1 - x2
        y12 = y1 - y2

        r = math.sqrt(x12 * x12 + y12 * y12)

        a1 = G * M2 / (r * r)
        a2 = G * M1 / (r * r)

        ax1 = - a1 * x12 / r
        ay1 = - a1 * y12 / r

        ax2 = a2 * x12 / r
        ay2 = a2 * y12 / r
        
        vx1 = vx1 + ax1 * time_step
        vy1 = vy1 + ay1 * time_step

        vx2 = vx2 + ax2 * time_step
        vy2 = vy2 + ay2 * time_step

        x1 = x1 + vx1 * time_step
        x2 = x2 + vx2 * time_step

        y1 = y1 + vy1 * time_step
        y2 = y2 + vy2 * time_step
    arcade.draw_circle_filled(x1, y1, 10, arcade.color.BLUE)
    arcade.draw_circle_filled(x2, y2, 50, arcade.color.RED)

def on_key_press(key, modifier):
    if key == arcade.key.Q:
        arcade.close_window()

def main():
    window = arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)

    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(draw, 1 / 100)

    window.on_key_press = on_key_press
    print('Press \'q\' to exit')

    arcade.run()

if __name__ == "__main__":
    main()

