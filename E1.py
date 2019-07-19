import pygame
from pygame import *
import math
import numpy as np
import random
import time

# click 1 thing for all data
# click another to clear screen
# change e size
# frame rate


pygame.init()
light_grey=(228, 233, 229)
dark_grey = (15,15,15)
black = (0,0,0)
yellow = (246,240,55)
white = (255,255,255)
red = (200,0,0)
screen_width = 800
screen_height = 600
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('electron simulator')
clock = pygame.time.Clock()

def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface, textSurface.get_rect()

def message_diplay(x,y, text, size,colour):
    largetext = pygame.font.Font('freesansbold.ttf', size) # make it large give it a font 
    TextSurf, TextRect = text_objects(text, largetext,colour)       # pygame basically makes a textbox for text
    TextRect.center  = (x,y)
    display.blit(TextSurf, TextRect)



class electron():
    def __init__(self,x,y,charge,speed_x,speed_y,electron_number):
        self.x = x
        self.y = y
        self.charge = charge
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.num = electron_number

    def force_between(self,x1,x2,y1,y2,charge1,charge2,e_0):
        x = x1-x2
        y = y1-y2
        r = (x,y)
        r_len = ((x**2)+(y**2))**0.5
        pi = 3.14159265358987
        if r_len == 0:
            pass
        else:
            F = ((charge1*charge2)/(4*pi*e_0))/(r_len**2)
            
            return(F)
        
        
    def draw_e(self,x,y):
        black=(0,0,0)
        pygame.draw.circle(display, yellow,(int(x), int(y)), 6,6)
        
    
def simulation():
    electron_dictionary = []
    click_delay = 0
    number_of_electrons = 4
    e = 1.0
    mass_e = 0.00005
    new_electron = False
    speed_y_0_box = screen_height*0.5
    side_bar = screen_width*0.95
    new_e_button_height = screen_height*0.05
    clear_button_y = screen_height*0.95
    for i in range(number_of_electrons):
        x=(random.uniform(0,screen_width))
        y=(random.uniform(0,screen_height))
        electron_dictionary.append(electron(x,y,e,0.0,0.0,i))
    a = 0
    no_walls = True
    while a < 9:
        display.fill(white)
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if new_electron == True:
                if mouse[0]<side_bar:
                    if click[0] == True and click_delay == 0:
                        click_delay+=1
                        new_electron = False
                        number_of_electrons+=1
                        electron_dictionary.append(electron(mouse[0],mouse[1],e,0,0,number_of_electrons))
            if mouse[0] > side_bar and mouse[1]<new_e_button_height:
                if click[0] == True and click_delay == 0:
                    new_electron = True
                    click_delay+=1
            if mouse[0] > side_bar and mouse[1]>clear_button_y:
                if click[0] == True and click_delay == 0:
                    electron_dictionary = []
            if mouse[0] > side_bar and speed_y_0_box<mouse[1]<speed_y_0_box +new_e_button_height:
                print("wwwwwwwwwwwwwwwwwwwww")
                if click[0] == True and click_delay == 0:
                    for i in electron_dictionary:
                        i.speed_x = 0
                        i.speed_y = 0
        if new_electron == True and mouse[0]<side_bar:
            pygame.draw.line(display, black,(mouse[0]-7,mouse[1]-7),(mouse[0]+7,mouse[1]+7),3) #
            pygame.draw.line(display, black,(mouse[0]-7,mouse[1]+7),(mouse[0]+7,mouse[1]-7),3)
        for i in electron_dictionary:
            i.draw_e(i.x,i.y)
            for j in electron_dictionary:
                if i != j:
                    if i.y - j.y != 0:
                        theta = math.atan((i.x-j.x)/(i.y-j.y))
                    else:
                        theta = 1
                    force = i.force_between(i.x,j.x,i.y,j.y,i.charge,j.charge,1.0)
                    dx = abs(i.x - j.x)
                    dy = abs(i.y - j.y)
                    if i.x > j.x and dy+dx != 0 :
                        i.speed_x += abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                    if i.x < j.x and dy+dx != 0:
                        i.speed_x += -abs((force/mass_e)*math.cos(theta))*(dx/(dy+dx))
                    if i.y > j.y and dy+dx != 0:
                        i.speed_y += abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                    if i.y < j.y and dy+dx != 0:
                        i.speed_y += -abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                    if no_walls == True:
                        if i.x>side_bar-1 and i.speed_x > 0:
                            i.x = 0
                        if  i.x<1 and i.speed_x < 0:
                            i.x = side_bar-1
        
                        if  i.y>screen_height-2 and i.speed_y > 0:
                            i.y = 0
                        if  i.y<1 and i.speed_y < 0:
                            i.y = screen_width
                    i.x += i.speed_x
                    i.y += i.speed_y
                    
            
                                
        if click_delay == 3:
            click_delay = 0
        if click_delay > 0:
            click_delay+=1
        pygame.draw.rect(display, light_grey,[side_bar, 0, 500, screen_height])            
        pygame.draw.rect(display, dark_grey,[side_bar, 0, 500, new_e_button_height])

        pygame.draw.rect(display, dark_grey,[side_bar, speed_y_0_box, 500, new_e_button_height])
        message_diplay(side_bar+ 20, 22 ,"add", 15, white)
        message_diplay(side_bar+ 20, speed_y_0_box + 22 ,"speed=0", 10, white)
        pygame.draw.rect(display, red,[side_bar, clear_button_y, 500, new_e_button_height])
        message_diplay(side_bar + 20, clear_button_y+20,"clear", 15, white)
        pygame.display.update()
        clock.tick(120)

simulation()
pygame.quit()
quit()
                                    
