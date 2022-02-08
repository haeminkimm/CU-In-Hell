# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joseph")

define e = Character(j)

init python:
    var = 1
    import pygame
    class TestDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.width = 10
            self.testsqr = Solid("#ffffff", xsize=self.width, ysize=30)

        def render(self, width, height, st, at):
            r2 = renpy.render(self.testsqr, 10, 10, 1, 1)
            # render.blit(self.testsqr, (0,0))
            r = renpy.Render(500,500)
            r.blit(r2, (0,0))
            self.width += 10
            self.testsqr = Solid("#ff00ff", xsize=self.width, ysize=30)
            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                self.testsqr = Solid("#00ff00", xsize=30, ysize=25)
                #return "chicken"
                return None
                # renpy.redraw(self, 0)
            raise renpy.IgnoreEvent()

    class ProtoTalk(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.box = Solid("#000000", xsize=100, ysize=30)
            self.phrase = "jf"
            self.question = "can I ask you something?"

        def render(self, width, height, st, at):
            r = renpy.Render(0,0)
            r.blit(renpy.render(self.box, 500, 500, 1, 1), (0,0))
            r.blit(renpy.render(Text(self.question), 500, 500, 1, 1), (10,0))
            return r

        def event (self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RIGHT:
                self.phrase = "rigth"
                renpy.redraw(self,0)

#This is the class that is actually used. the rest i dont think are at all

    class sizeTest(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.shape = Solid("#222222",xsize=600,ysize=300)
            self.question = "can i ask you somethign?"
            self.answer = " "
            self.t = 0
            self.starting = 0
            self.timeover = None
            self.test = False
            self.leftans = "yes"
            self.rightans = "no"
            self.leftresp = self.yesresp
            self.rightresp = self.noresp
            self.animal = None

        def render(self,width,height,st,at):
            r = renpy.Render(width,height)
            r.blit(renpy.render(self.shape,width,height,st,at), (width/2-300,height-330))
            r.blit(renpy.render(Text(self.question),width,height,st,at), (width/2-300,height-380))
            r.blit(renpy.render(Text(self.answer),width,height,st,at), (width/2,height-30))
            self.t -= (pygame.time.get_ticks() - self.starting)/1000
            if self.t < 0 and self.timeover:
                self.timeover()
            renpy.redraw(self,0)
            return r

        def event(self,ev,x,y,st):
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RIGHT:
                self.answer = self.rightans
                self.t = 3
                self.starting = pygame.time.get_ticks()
                self.timeover = self.rightresp
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_LEFT:
                self.answer = self.leftans
                self.t = 3
                self.starting = pygame.time.get_ticks()
                self.timeover = self.leftresp
            if self.animal:
                return self.animal

        def noresp(self):
            # self.test = True
            # renpy.timeout(0)
            self.answer = " "
            renpy.jump("saidno")

        def yesresp(self):
            self.question = "cats or dogs?"
            self.answer = " "
            self.leftans = "cats"
            self.rightans = "dogs"
            self.leftresp = self.catresp
            self.rightresp = self.dogresp

        def catresp(self):
            self.animal = "cat"
            renpy.timeout(0)

        def dogresp(self):
            self.animal = "dog"
            renpy.timeout(0)

screen test:
    text "testing"
    # button:
    #     action Return()
    #     at transform:
    #         xpos 0.5
    #         ypos 0.5
    #         xsize 100
    add sizeTest():
        xalign 0.5
        yalign 0.5


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    e "Hey, can i ask you something?"


    hide window
    call screen test

    e "this was var [var]"

    $var = _return

    e "I hate [var]s"

    e "I hope I never see you again"

    # This ends the game.

    return

label saidno:
    e "oh..."

    return

label saidpet:
    e "I hate [var]s"

    e "I hope i never see you again"

    return
