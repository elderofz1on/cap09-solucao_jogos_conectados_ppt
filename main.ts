radio.onReceivedNumber(function (receivedNumber) {
    basic.pause(200)
    if (receivedNumber == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (receivedNumber == 2) {
        basic.showIcon(IconNames.Square)
    } else if (receivedNumber == 3) {
        basic.showIcon(IconNames.Scissors)
    }
    basic.pause(300)
    if (jogador1 == receivedNumber) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            `)
        basic.pause(300)
        basic.showNumber(game.score())
    } else {
        if (jogador1 == 1 && receivedNumber == 3) {
            game.addScore(1)
            basic.showLeds(`
                . . # . .
                . # # # .
                # # # # #
                . . . . .
                . . . . .
                `)
            basic.pause(300)
            basic.showNumber(game.score())
        } else {
            if (jogador1 == 2 && receivedNumber == 1) {
                game.addScore(1)
                basic.showLeds(`
                    . . # . .
                    . # # # .
                    # # # # #
                    . . . . .
                    . . . . .
                    `)
                basic.pause(300)
                basic.showNumber(game.score())
            } else {
                if (jogador1 == 3 && receivedNumber == 2) {
                    game.addScore(1)
                    basic.showLeds(`
                        . . # . .
                        . # # # .
                        # # # # #
                        . . . . .
                        . . . . .
                        `)
                    basic.pause(300)
                    basic.showNumber(game.score())
                } else {
                    basic.showLeds(`
                        . . . . .
                        . . . . .
                        # # # # #
                        . # # # .
                        . . # . .
                        `)
                    basic.pause(300)
                    basic.showNumber(game.score())
                }
            }
        }
    }
})
input.onGesture(Gesture.Shake, function () {
    jogador1 = randint(1, 3)
    if (jogador1 == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (jogador1 == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    basic.pause(300)
    radio.sendNumber(jogador1)
})
input.onButtonPressed(Button.AB, function () {
    game.setScore(0)
    basic.showNumber(game.score())
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(game.score())
})
let jogador1 = 0
radio.setGroup(100)
basic.showString("Agite para jogar")
game.setScore(0)
