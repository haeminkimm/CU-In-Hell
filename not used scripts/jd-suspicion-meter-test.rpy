#first, need to declare python with init python and import pygame

init python:
    import pygame
    class testSuspension(renpy.Displayable):
        def __init__(self):
            #constructor equivalent
            self.name = 'hello world'
            self.width = 200
            self.height = 200

        def render(self, width, height, st, at):
            #draws when the class is called
            #to redraw multiple times, utilize renpy.redraw() at the end
            r = renpy.Render(self.width, self.height)
            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            #used to pass a pygame event in
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                myfont = pygame.font.SysFont("Comic Sans MS", 18)
                text = myfont.render("this is complete ass", 1, black)
                r.blit(text, 50, 50)

# now we're in renpy land

screen testDisplayable:
    text "super test boy"
    #this is to add the displayable class in
    add testSuspension():
        xalign 0.1
        yalign 0.1


define j = Character('test boy')

label start:
    scene bg room
    j "whats good slime"

    #hide window to before you call the screen testDisplayable
    hide window
    call screen testDisplayable

    return
