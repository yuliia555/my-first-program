def on_button_pressed_a():
    basic.show_string("Hi!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Bye!")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.GHOST)

def on_forever():
    pass
basic.forever(on_forever)
