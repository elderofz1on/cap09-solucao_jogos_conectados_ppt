def on_received_number(receivedNumber):
    basic.pause(200)
    if receivedNumber == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif receivedNumber == 2:
        basic.show_icon(IconNames.SQUARE)
    elif receivedNumber == 3:
        basic.show_icon(IconNames.SCISSORS)
    basic.pause(300)
    if jogador1 == receivedNumber:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # #
                        . . . . .
                        . . . . .
        """)
        basic.pause(300)
        basic.show_number(game.score())
    elif jogador1 == 1 and receivedNumber == 3:
        game.add_score(1)
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # # # # #
                        . . . . .
                        . . . . .
        """)
        basic.pause(300)
        basic.show_number(game.score())
    elif jogador1 == 2 and receivedNumber == 1:
        game.add_score(1)
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # # # # #
                        . . . . .
                        . . . . .
        """)
        basic.pause(300)
        basic.show_number(game.score())
    elif jogador1 == 3 and receivedNumber == 2:
        game.add_score(1)
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # # # # #
                        . . . . .
                        . . . . .
        """)
        basic.pause(300)
        basic.show_number(game.score())
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # #
                        . # # # .
                        . . # . .
        """)
        basic.pause(300)
        basic.show_number(game.score())
radio.on_received_number(on_received_number)

def on_gesture_shake():
    global jogador1
    jogador1 = randint(1, 3)
    if jogador1 == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif jogador1 == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
    basic.pause(300)
    radio.send_number(jogador1)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    game.set_score(0)
    basic.show_number(game.score())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(game.score())
input.on_button_pressed(Button.B, on_button_pressed_b)

jogador1 = 0
radio.set_group(100)
basic.show_string("Agite para jogar")
game.set_score(0)