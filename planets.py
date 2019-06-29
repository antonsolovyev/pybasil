import math
import arcade

# Screen dimension constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
TITLE ='Planet simulator'

# Physics constants
M1 = 1
M2 = 25
G = 1e4
TICK_STEPS = 500

# Variables
x1 = 800
y1 = 380

x2 = 300
y2 = 380

vx1 = 0
vy1 = 15

vx2 = 0
vy2 = - vy1 * M1 / M2 # Ensure center mass has 0 initial velocity

def draw(time_delta):
    arcade.start_render()
    global x1, x2, y1, y2, vx1, vx2, vy1, vy2
    for i in range(0, TICK_STEPS):
        r = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        a1 = G * M2 / (r * r)
        a2 = G * M1 / (r * r)
        ax1 = - a1 * (x1 - x2) / r
        ay1 = - a1 * (y1 - y2) / r
        ax2 = a2 * (x1 - x2) / r
        ay2 = a2 * (y1 - y2) / r
        vx1 = vx1 + ax1 * (1 / TICK_STEPS)
        vx2 = vx2 + ax2 * (1 / TICK_STEPS)
        vy1 = vy1 + ay1 * (1 / TICK_STEPS)
        vy2 = vy2 + ay2 * (1 / TICK_STEPS)
        x1 = x1 + vx1 * (1 / TICK_STEPS)
        x2 = x2 + vx2 * (1 / TICK_STEPS)
        y1 = y1 + vy1 * (1 / TICK_STEPS)
        y2 = y2 + vy2 * (1 / TICK_STEPS)
    arcade.draw_circle_filled(x1, y1, 5, arcade.color.BLUE)
    arcade.draw_circle_filled(x2, y2, 25, arcade.color.RED)

def on_key_press(key, modifier):
    if key == arcade.key.Q:
        arcade.close_window()

def main():
    window = arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)

    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(draw, 1 / 50)

    window.on_key_press = on_key_press
    print('Press \'q\' to exit')

    arcade.run()

if __name__ == "__main__":
    main()

