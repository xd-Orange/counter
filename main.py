count = 0

def on_button_pressed_a():
    global count
    count = 5
    for index in range(6):
        basic.show_number(count)
        count += -1
input.on_button_pressed(Button.A, on_button_pressed_a)
