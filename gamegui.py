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
    def __init__(self):
        
        pass
    def draw(self):
        self.screen.fill(0,0,0)
        
class Charecter(ABC):
    @abstractmethod
    def properties(self):
        self.x
        self.y
        self.health
        self.size
        
class NPC():
    def __init__(self):
        self.y = Screen_Y/2
        self.x = Screen_X
        self.health = 300
        self.rad = 20.0
        self.circle = []
    def init_circle(self):  # Clear screen
        for x in range(50, 1300, 80):
            for y in range(300, 0, -80):
                self.circle.append([x,y])


class Game(NPC,Menu):
    def __init__(self):
        super().__init__()# to initialise the concrete method
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
        for rocket_pos in self.rocket_pos:
            rocket_pos[1] -= 18
            if rocket_pos[1] > 750:
                rocket_pos = None 
                        
    def run(self):
        while self.running:
            self.gameevents()
            self.update()
            no_circle = self.collision_detection(self.npc1)
            if (no_circle):
                self.circle.remove(no_circle)
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
        NPC.init_circle(self)
        for circle in self.circle:
            pg.draw.circle(self.screen,(255,255,255),(circle[0],circle[1]),25.0)
        pg.display.flip()
    def collision_detection(self,npc1):
        for rocket in self.rocket_pos:
            rocket_start = (rocket[0],rocket[1])
            rocket_end = (rocket[0], rocket[1]+ 50)
            for circle in self.circle:
                dist_start = math.sqrt((rocket_start[0]- npc1.x)**2 + (rocket_start[1] - npc1.y)**2)
                dist_end = math.sqrt((rocket_end[0]- npc1.x)**2 + (rocket_end[1] - npc1.y)**2)
                if(dist_start <= 25 or dist_end <= 25):
                    return circle
        return None
            
        

# Usage
if __name__ == "__main__":
    game = Game()
    game.run()