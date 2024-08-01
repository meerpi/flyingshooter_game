import pygame as pg
import math
from abc import ABC,abstractmethod
from enum import Enum,auto
Screen_X = 1300
Screen_Y = 800
class Gamestate(Enum) :
    menu = auto()
    playing = auto()
    paused = auto()
    gameover = auto()
    
class Menu:
    #    pass
    pass
class Charecter(ABC):
    @abstractmethod
    def properties(self):

        pass
        
class NPC:
    def __init__(self):
        self.y = Screen_Y/2
        self.x = Screen_X
        self.health = 300
        self.rad = 20.0
        self.circles = []
        self.init_circle()

    def init_circle(self):
        for x in range(50, 1300, 80):
            for y in range(300, 0, -80):
                self.circles.append([x, y])
    def init_attack(self):
        for x in range():
            pass


class Game(NPC,Menu):
    def __init__(self):
        NPC.__init__(self)# to initialise the concrete method
        pg.init()
        self.screen = pg.display.set_mode((Screen_X,Screen_Y)) 
        self.clock = pg.time.Clock()
        self.running = True
        self.state = Gamestate.playing
        self.x = 350
        self.y = 750
        self.rocket_pos = []# just for rocket position initialising and staying as null need list for multiple rockets to exsist at same time
        self.npc1 = NPC()
    def gameevents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False 
                    
            if pg.K_ESCAPE :
                self.state = Gamestate.menu
                #go to menu
                pass
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.rocket_pos.append([self.x + 50 ,self.y])#append starting point of each rocket in arrey.
            
                
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.x > 0:
            self.x -= 14
        if keys[pg.K_d] and self.x < 1200:
            self.x += 14
        if keys[pg.K_w] and self.y > 0 :
            self.y -= 14
        if keys[pg.K_s] and self.y < 750:
            self.y += 14
    def rocket_work(self): 
        for rocket in self.rocket_pos[:]:
            rocket[1] -= 18
            if rocket[1] < 0:
                self.rocket_pos.remove(rocket)
            elif(self.collision_detection(rocket)):
                self.rocket_pos.remove(rocket)
                
    def collision_detection(self,rocket):
        rocket_start = (rocket[0],rocket[1])
        rocket_end = (rocket[0], rocket[1]+ 50)
        for circle in self.npc1.circles[:]:
            dist_start = math.sqrt((rocket_start[0]- circle[0])**2 + (rocket_start[1] - circle[1])**2)
            dist_end = math.sqrt((rocket_end[0]- circle[0])**2 + (rocket_end[1] - circle[1])**2)
            if(dist_start <= 25 or dist_end <= 25):
                self.npc1.circles.remove(circle)
                return True
        return False

    def run(self):
        while self.running:
            self.gameevents()
            self.update()
            self.rocket_work()
            self.draw()
            self.clock.tick(60)
        self.cleanup()
    
    def cleanup(self):
        pg.quit()
        
    def draw(self):#not finished draw thje rocket
        self.screen.fill((0,0,0))
        x = self.x
        y = self.y
        pg.draw.rect(self.screen,(255,255,255),(x,y,100,50),3 )
        for rocket in self.rocket_pos:
            pg.draw.line(self.screen,(255,255,255),(rocket[0],rocket[1]),(rocket[0],rocket[1]+50))
        for circle in self.npc1.circles:
            pg.draw.circle(self.screen, (255, 255, 255), (circle[0], circle[1]), 25.0)
        pg.display.flip()

# Usage
if __name__ == "__main__":
    game = Game()
    game.run()