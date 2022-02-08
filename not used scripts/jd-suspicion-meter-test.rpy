#first, need to declare python with init python and import pygame

init python:
    import pygame
    class testSuspension(renpy.Displayable):
        def __init__(self):
            #constructor equivalent
            super(testSuspension, self).__init__()
            self.name = 'hello world'
            self.width = 600
            self.height = 300

        def render(self, width, height, st, at):
            #draws when the class is called
            #to redraw multiple times, utilize renpy.redraw() at the end
            r = renpy.Render(self.width, self.height)

            r.blit(renpy.render(Solid('#000000', xsize=self.width, ysize=self.height), width, height, st, at), (0,0))

            r.blit(renpy.render(Text(self.name), width, height, st, at), (0, 50))

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            #used to pass a pygame event in
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                self.name = 'this should change when i press space'

# now we're in renpy land

screen testDisplayable:
    text "super test boy":
        xalign 0.5
        yalign 0.5
        ypos config.screen_height/2 - 170
    #this is to add the displayable class in
    add testSuspension():
        xalign 0.5
        yalign 0.5

define j = Character('test boy')

label start:
    scene bg room
    j "whats good slime"

    #hide window to before you call the screen testDisplayable
    hide window
    call screen testDisplayable

    return
