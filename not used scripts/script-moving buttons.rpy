# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Eileen")
define e = Character(j)
define me = Character("me")

transform t:
    xalign 0.5
    yalign 0.5
    zoom 0.25

screen word():
    text "hi"

screen diabut(resp, xStart, yStart, xMax = 1, yMax = 1, xMin = 0, yMin = 0, pic = "square.png", locStepSize = 0.07):
    python:
        def move_right(stepSizeLoc, trans, st, at):
            trans.xalign += stepSizeLoc
        def move_left(stepSizeLoc, trans, st, at):
            trans.xalign -= stepSizeLoc
        def move_up(trans, st, at):
            trans.yalign -= stepSize
        def move_down(trans, st, at):
            trans.yalign += stepSize
        move_right_curry = renpy.curry(move_right)
        move_left_curry = renpy.curry(move_left)
    imagebutton:
        idle pic
        action resp
        at transform:
            size(80,80)
            xalign xStart
            yalign yStart
            parallel:
                block:
                    pause 0.
                    function move_right_curry(locStepSize)
                    repeat ((xMax-xStart) * (1 / locStepSize))
                block:
                    block:
                        pause 0.
                        function move_left_curry(locStepSize)
                        repeat (xMax - xMin) * (1 / locStepSize)
                    block:
                        pause 0.
                        function move_right_curry(locStepSize)
                        repeat (xMax - xMin) * (1 / locStepSize)
                    repeat
            parallel:
                block:
                    pause 0.
                    function move_up
                    repeat ((yMax-yStart) * (1 / stepSize))
                block:
                    block:
                        pause 0.
                        function move_down
                        repeat (yMax - yMin) * (1 / stepSize)
                    block:
                        pause 0.
                        function move_up
                        repeat (yMax - yMin) * (1 / stepSize)
                    repeat

screen test():
    # add "square.png" xalign 0.5 yalign 0.9 size (800, 300)
    use diabut([SetVariable("var","penguins"), Return()], 0.3, 0.5, 0.7, 0.5, 0.3, 0, "penguin.png", stepSize)
    use diabut([SetVariable("var","raccoons"), Return()], 0.5, 0.5, 0.7, 0.5, 0.3, 0, "raccoon.png", 0.01)


screen vboxtest():
    vbox:
        text "top"
        text "bottom"

# image testgrounds:
#     Text("1")
#     parallel:
#         xalign 0.0
#         linear 1.3 xalign 1.0
#         linear 1.3 xalign 0.0
#         repeat
#     parallel:
#         yalign 0.0
#         linear 1.6 yalign 1.0
#         linear 1.6 yalign 0.0
#         repeat

# The game starts here.
# this is here to make it so buttons are activated on mouse down instead of mouse up
# for snappier button actions since its timing based gameplay
init:
    $ config.keymap['button_ignore'].remove('mousedown_1')
    $ config.keymap['button_select'].append('mousedown_1')
    $ config.keymap['button_select'].remove('mouseup_1')
    $ config.keymap['dismiss'].remove('mouseup_1')
    $ config.keymap['dismiss'].append('mousedown_1')

label start:
    $ var = 1
    $ stepSize = 0.007

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # show screen vboxtest()
    scene bg room
    show eileen happy at left
    show eileen happy at right

    # with dissolve



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at left

    # These display lines of dialogue.

    j "This is not going well"

    j "raccoons or penguins"

    # call screen test
    window hide
    hide eileen happy
    $renpy.call_screen("test")


    me "I like [var]"

    if _return == "dogs":
        j "I love dogs"
    else:
        j "ok"

    # This ends the game.

    return
