let count = 0
input.onButtonPressed(Button.A, function () {
    count = 5
    for (let index = 0; index < 6; index++) {
        basic.showNumber(count)
        count += -1
    }
})
