
from kivy.graphics import *
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.graphics import Line

__author__ = 'Dominik'
from kivy.uix import *


class Keyboard(Widget):
    '''
    Klasa pozwalajaca na obsluge programu z klawiatury
    '''
    def __init__(self, **kwargs):
        super(Keyboard, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.vel_x=0
        self.vel_y=0

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            # self.player1.center_y += 10
            print "pressed"
        elif keycode[1] == 'up':
            self.vel_y+=0.5
            print "pressed"
        elif keycode[1] == 'down':
            self.vel_y-=0.5
            print "pressed"
        elif keycode[1] == 'right':
            self.vel_x+=0.5
        elif keycode[1] == 'left':
            self.vel_x-=0.5
        return True


class Pilka(Widget):
    '''
    Obiekt reprezentujacy pilke
    '''
    keyb=Keyboard()
    vel_x=0
    vel_y=0

    def move(self):
        velocity_x = self.keyb.vel_x
        velocity_y = self.keyb.vel_y
        velocity = Vector(velocity_x,velocity_y)
        self.pos=velocity+self.pos

    def set_it(self):
        self.pos = 100, 100
        self.size = 50, 50

    # def check_collide(self,obstacle1,obstacle2):
    #     if(self.collide_widget(obstacle1) or self.collide_widget(obstacle2)):
    #         return True
    #     else:
    #         return False

    def increase_xval(self):
        self.x_vel_value+=10

    def decrease_xval(self):
        self.x_vel_value-=10

    def on_touch_down(self, touch):
        '''
        metoda ta pozwala na obsluge programu z poziomu dotyku
        '''
        if(self.center_x<touch.x):
            self.keyb.vel_x+=0.1
        else:
            self.keyb.vel_x-=0.1
        if(self.center_y<touch.y):
            self.keyb.vel_y+=0.1
        else:
            self.keyb.vel_y-=0.1

class KulkaGame(Widget):
    '''
    Obiekt reprezentujacy gre
    '''
    ball=Pilka()#ObjectProperty()
    belka=ObjectProperty()
    points=NumericProperty()
    # list1=[77, 67, 730, 67, 730, 600,480,600,480,350,438,350,438,550,204,550,204,480,0,480]
    # list2=[77, 167, 630, 167, 630, 500,580,500,580,250,338,250,338,450,304,450,304,380,0,380]
    # linia1=MyLine()
    # linia2=MyLine()

    # wg=MyLine()
    # wg.make_rectangle()

    def make_level1(self):
        '''
        metoda pozwalajaca na stworzenie poziomu pierwszego

        '''
        list1=[0, 67, 730, 67, 730, 600,480,600,480,350,438,350,438,550,204,550,204,480,0,480]
        list2=[0, 167, 630, 167, 630, 500,580,500,580,250,338,250,338,450,304,450,304,380,0,380]

        # with self.wg.canvas:
        #      self.wg.line1=Line(points=self.list1, width=10)
        with self.canvas:
            Color(1., 1., 0)
            Line(points=list1, width=10)
            Line(points=list2, width=10)

        # self.belka.set_it()
##zrobic kolizje !!!!!!!!!!!!!!!!
    # def check_for_collisions(self):
    #     for i in range(0,len(self.list1)):
    #         if(self.ball.center>self.list1[i] and self.ball.center<self.list1[i+1] and self.ball.center>self.list1[i] and self.ball.center<self.list1[i+1])
    #     return False

    def set_ball_position(self):
        '''
        ustawienie pozycji pilki

        '''
        self.ball.set_it()

    def check_level1(self):
        '''
        metoda pozwalajaca na kontrole poziomu pierwszego

        '''
        # print self.ball.x
        # print self.ball.y
        if(self.ball.x>0 and self.ball.x<10 and self.ball.y>380 and self.ball.y<480):
            self.ball.pos = 100, 100
            self.ball.vel_x=0
            self.ball.vel_y=0
            self.points+=1


    def update(self,dt):
        '''
        metoda odswierzajaca gre
        :param dt: parametr delta time ( oznaczajacy) co ile dana metoda ma sie wykonac

        '''
        self.ball.move()
        self.check_level1()


        # print self.ball.collide_widget(self.linia1)#.check_collide(self.linia1,self.linia2)







class KulkaApp(App):

    def build(self):
        '''
        budowanie aplikacji
        :return: obiekt gra
        '''
        game=KulkaGame()
        game.set_ball_position()
        game.make_level1()
        Clock.schedule_interval(game.update,1/20000.0)
        return game


if __name__=="__main__":
    KulkaApp().run()