from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
button_press = False

white = [255, 255, 255]
black = [0, 0, 0]

while True:
    event = sense.stick.wait_for_event()
    # User pressed the button
    if event.action == "pressed" and event.direction == "middle":
        display = []
        # Display is off, turn it on
        if button_press:
            button_press = False
            colour = black
        # Display is on, turn it off
        else:
            button_press = True
            colour = white

        for i in range(64):
            display.append(colour)

        sense.set_pixels(display)
        sleep(0.1)
