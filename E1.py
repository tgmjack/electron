import pygame
from pygame import *
import math
import numpy as np
import random
import time
## to do list
# fix quit error
# click 1 thing for all data speeds and positions
# frame rate button
# fix constants
# get to run without python


pygame.init()
light_grey=(228, 233, 229)
dark_grey = (15,15,15)
black = (0,0,0)
yellow = (246,240,55)
light_blue = (135,206,250)
green = (0, 200, 0)
white = (255,255,255)
red = (200,0,0)
screen_width = 1100.0
screen_height = 700.0
display = pygame.display.set_mode((int(screen_width), int(screen_height)))
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
        r_len = ((x**2)+(y**2))**0.5
        pi = 3.14159265358987
        if r_len == 0:
            pass
        else:
            F = ((charge1*charge2)/(4*pi*e_0))/(r_len**2)
            return(F)
        
    def draw_e(self,x,y):
        pygame.draw.circle(display, yellow,(int(x), int(y)), 6,6)

class positron(electron):
    def __init__(self,x,y,charge,speed_x,speed_y,electron_number):
        self.x = x
        self.y = y
        self.charge = charge
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.num = electron_number
        
    def draw_p(self,x,y):
        pygame.draw.circle(display, red,(int(x), int(y)), 6,6)
    
def simulation():
    click_delay = 0
    electrons = []
    number_of_electrons = 1
    walls_button_y = screen_height*0.3
    bring_back_button_y = screen_height * 0.1
    bring_back_y =  bring_back_button_y
    e = -1.0
    y_list_ticker=0
    mass_e = 0.002
    too_far = 400
    wall_charge = -1.0
    new_positron_y = screen_height *0.8
    new_electron = False
    new_positron = False
    speed_y_0_box = screen_height*0.5
    side_bar = screen_width*0.95
    new_e_button_height = screen_height*0.05
    wall_charge_button = screen_height*0.4
    choose_new_wall_charge = False
    clear_button_y = screen_height*0.95
    positrons = []
    for i in range(number_of_electrons):
        x=(random.uniform(0,screen_width))
        y=(random.uniform(0,screen_height))
        electrons.append(electron(x,y,e,0.0,0.0,i))
          #(self,x,y,charge,speed_x,speed_y,electron_number):
    a = 0
    no_walls = True
    number_of_positrons = 1
    for p in range(number_of_positrons):
        x=(random.uniform(0,screen_width))
        y=(random.uniform(0,screen_height))
        positrons.append(positron(x,y,-e,0.0,0.0,i))
    while a < 9:
        display.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                a = 11
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if new_electron == True:
                if mouse[0]<side_bar:
                    if click[0] == True and click_delay == 0:
                        click_delay+=1
                        new_electron = False
                        number_of_electrons+=1
                        electrons.append(electron(mouse[0],mouse[1],e,0,0,number_of_electrons))

            if new_positron == True:
                if mouse[0]<side_bar:
                    if click[0] == True and click_delay == 0:
                        click_delay+=1
                        new_positron = False
                        number_of_positrons+=1
                        positrons.append(positron(mouse[0],mouse[1],e,0,0,number_of_positrons))
                        
            if mouse[0] > side_bar and mouse[1]<new_e_button_height:
                if click[0] == True and click_delay == 0:
                    new_electron = True
                    click_delay+=1
            if mouse[0] > side_bar and mouse[1]>clear_button_y:
                if click[0] == True and click_delay == 0:
                    electrons = []
                    number_of_electrons = 0
                    positrons = []
                    number_of_positrons = 0
            if mouse[0] > side_bar and new_positron_y < mouse[1] < new_positron_y + new_e_button_height:
                if click[0] == True and click_delay == 0:
                    new_positron = True
                    click_delay+=1
                    
            if mouse[0] > side_bar and speed_y_0_box<mouse[1]<speed_y_0_box +new_e_button_height:
                if click[0] == True and click_delay == 0:
                    for i in electrons:
                        i.speed_x = 0
                        i.speed_y = 0
                    for p in positrons:
                        p.speed_x = 0
                        p.speed_y = 0
                        
            if mouse[0] > side_bar and walls_button_y<mouse[1]<walls_button_y +new_e_button_height:
                print("wwwwwwwwwwwwwwwwwwwww")
                if click[0] == True and click_delay == 0 and no_walls == True:
                    no_walls = False
                    print("333333")
                    click_delay+=1
                if click[0] == True and click_delay == 0 and no_walls == False:
                    no_walls = True
                    click_delay+=1
                    print("44444")
            if mouse[0] > side_bar and wall_charge_button<mouse[1]<wall_charge_button +new_e_button_height:
                if click[0] == True and click_delay == 0 and choose_new_wall_charge == False:
                    click_delay+=1
                    choose_new_wall_charge= True
                if click[0] == True and click_delay == 0 and choose_new_wall_charge == True:
                    click_delay+=1
                    choose_new_wall_charge= False

            if mouse[0] > side_bar and bring_back_y<mouse[1]<bring_back_y +new_e_button_height:
                if click[0] == True and click_delay == 0:
                    click_delay+=1
                    for i in electrons:
                        if i.x > side_bar:
                            i.x = random.randint(screen_width*0.2,screen_width*0.8)
                        if i.x < 0:
                            i.x = random.randint(screen_width*0.2,screen_width*0.8)
                        if i.y > screen_height:
                            i.y = random.randint(screen_height*0.2,screen_height*0.8)
                        if i.y < 0:
                            i.y = random.randint(screen_height*0.2,screen_height*0.8)
                    for i in positrons:
                        if i.x > side_bar:
                            i.x = random.randint(screen_width*0.2,screen_width*0.8)
                        if i.x < 0:
                            i.x = random.randint(screen_width*0.2,screen_width*0.8)
                        if i.y > screen_height:
                            i.y = random.randint(screen_height*0.2,screen_height*0.8)
                        if i.y < 0:
                            i.y = random.randint(screen_height*0.2,screen_height*0.8)
            if choose_new_wall_charge==True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_0:
                        wall_charge = -0.0
                        choose_new_wall_charge=False
                    if event.key == K_1:
                        wall_charge = -1.0
                        choose_new_wall_charge=False
                    if event.key == K_2:
                        wall_charge = -2.0
                        choose_new_wall_charge=False
                    if event.key == K_3:
                        wall_charge = -3.0
                        choose_new_wall_charge=False
                    if event.key == K_4:
                        wall_charge = -4.0
                        choose_new_wall_charge=False
                    if event.key == K_5:
                        wall_charge = -5.0
                        choose_new_wall_charge=False
                    if event.key == K_6:
                        wall_charge = -6.0
                        choose_new_wall_charge=False
                    if event.key == K_7:
                        wall_charge = -7.0
                        choose_new_wall_charge=False
                    if event.key == K_8:
                        wall_charge = -8.0
                        choose_new_wall_charge=False
                    if event.key == K_9:
                        wall_charge = -9.0
                        choose_new_wall_charge=False
                    
        if new_electron == True and mouse[0]<side_bar:
            pygame.draw.line(display, yellow,(mouse[0]-7,mouse[1]-7),(mouse[0]+7,mouse[1]+7),3) #
            pygame.draw.line(display, yellow,(mouse[0]-7,mouse[1]+7),(mouse[0]+7,mouse[1]-7),3)
        if new_positron == True and mouse[0]<side_bar:
            pygame.draw.line(display, red,(mouse[0]-7,mouse[1]-7),(mouse[0]+7,mouse[1]+7),3) #
            pygame.draw.line(display, red,(mouse[0]-7,mouse[1]+7),(mouse[0]+7,mouse[1]-7),3)

        for i in electrons:
            i.draw_e(i.x,i.y)
    
            for j in electrons:
                if i != j:
                    if i.y - j.y != 0:
                        theta = math.atan((i.x-j.x)/(i.y-j.y))
                    else:
                        theta = 1
                    force = float(i.force_between(i.x,j.x,i.y,j.y,i.charge,j.charge,1.0))
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
                        i.x = 0.0
                    if  i.x<1 and i.speed_x < 0:
                        i.x = float(side_bar-1 )       
                    if  i.y>screen_height-2 and i.speed_y > 0:
                        i.y = 0.0
                    if  i.y<1 and i.speed_y < 0:
                        i.y = float(screen_height)
                            #force_between(self,x1,x2,y1,y2,charge1,charge2,e_0):
                if no_walls == False:
                    if 0<i.x < side_bar/2:
                        force = float(i.force_between(i.x,0,i.y,i.y,i.charge,wall_charge,1.0))
                        i.speed_x += abs(force/mass_e)
                        
                    if i.x < 0:
                        i.x = 2.0
                    if side_bar> i.x > side_bar/2:
                        force = float(i.force_between(i.x,side_bar,i.y,i.y,i.charge,wall_charge,1.0))
                        i.speed_x += -abs(force/mass_e)
                    if i.x > side_bar :
                        i.x = float(side_bar - 2.0)
                    if screen_height > i.y > screen_height/2:
                        force = i.force_between(i.x,i.x,i.y,screen_height,i.charge,wall_charge,1.0)
                        i.speed_y += float(-abs(force/mass_e))
                    if i.y > screen_height:
                        i.y = float(screen_height - 2.0)
                    if 0<i.y < screen_height/2:
                        force = i.force_between(i.x,i.x,i.y,0,i.charge,wall_charge,1.0)
                        if type(force) is None:
                            force = 0.0
                        i.speed_y += float(abs(force/mass_e))
                    if i.y < 0:
                        i.y = 2.0
                    
                if no_walls == True:
                    if i.x < 0:
                        i.x = side_bar
                    if i.x > side_bar:
                        i.x = 0
                    if i.y > screen_height:
                        i.y = 1
                    if i.y < 0:
                        i.y = screen_height -1
                i.x += i.speed_x
                i.y += i.speed_y
                if i.y < 1:
                    i.y = screen_height

        
        for p in positrons:
            p.draw_p(p.x,p.y)            
            for j in electrons:
                if p.y - j.y != 0:
                    theta = math.atan((p.x-j.x)/(p.y-j.y))
                else:
                    theta = 1
                force = p.force_between(p.x,j.x,p.y,j.y,p.charge,j.charge,1.0)
                dx = abs(p.x - j.x)
                dy = abs(p.y - j.y)
                if p.x > j.x and dy+dx != 0 :
                    p.speed_x += -abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                    j.speed_x +=abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                if p.x < j.x and dy+dx != 0:
                    p.speed_x += abs((force/mass_e)*math.cos(theta))*(dx/(dy+dx))
                    j.speed_x += -abs((force/mass_e)*math.cos(theta))*(dx/(dy+dx))
                if p.y > j.y and dy+dx != 0:
                    p.speed_y += -abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                    j.speed_y += abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                if p.y < j.y and dy+dx != 0:
                    p.speed_y += abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                    j.speed_y += -abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))

            for z in positrons:
                if p != z:
                    if p.y - z.y != 0:
                        theta = math.atan((p.x-z.x)/(p.y-z.y))
                    else:
                        theta = 1
                    force = p.force_between(p.x,z.x,p.y,z.y,p.charge,z.charge,1.0)
                    dx = abs(p.x - z.x)
                    dy = abs(p.y - z.y)
                    if p.x > z.x and dy+dx != 0 :
                        p.speed_x += abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                        z.speed_x += -abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                    if p.x < z.x and dy+dx != 0:
                        p.speed_x += -abs((force/mass_e)*math.cos(theta))*(dx/(dy+dx))
                        z.speed_x += abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                    if p.y > z.y and dy+dx != 0:
                        p.speed_y += abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                        z.speed_y += -abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                    if p.y < z.y and dy+dx != 0:
                        p.speed_y += -abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                        z.speed_y += abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                if no_walls == True:
                    if p.x>side_bar-1 and p.speed_x > 0:
                        p.x = 0.0
                    if  p.x<1 and p.speed_x < 0:
                        p.x = float(side_bar-1 )       
                    if  p.y>screen_height-2 and p.speed_y > 0:
                        p.y = 0.0
                    if  p.y<1 and p.speed_y < 0:
                        p.y = float(screen_height)
                            #force_between(self,x1,x2,y1,y2,charge1,charge2,e_0):
                if no_walls == False:
                    if p.x != 0:
                        if 0<p.x < side_bar/2 :
                            force = float(p.force_between(p.x,0,p.y,p.y,p.charge,wall_charge,1.0))
                            p.speed_x += -abs(force/mass_e)    
                        if p.x < -too_far:
                            p.x = 2.0
                        if -too_far < p.x < 0:
                            force = float(p.force_between(p.x,0,p.y,p.y,p.charge,wall_charge,1.0))
                            p.speed_x += -abs(force/mass_e)


                    if p.x != side_bar:
                        if side_bar >p.x > side_bar/2 :
                            force = float(p.force_between(p.x,side_bar,p.y,p.y,p.charge,wall_charge,1.0))
                            p.speed_x += abs(force/mass_e)
                        if p.x > side_bar + too_far:
                            p.x = float(side_bar - 2)
                        if side_bar < p.x < side_bar + too_far:
                            force = float(p.force_between(p.x,side_bar,p.y,p.y,p.charge,wall_charge,1.0))
                            p.speed_x +=  -abs(force/mass_e)
                        

                    if p.y != screen_height:
                        if screen_height>p.y > screen_height/2 :
                            force = p.force_between(p.x,p.x,p.y,screen_height,p.charge,wall_charge,1.0)
                            p.speed_y += abs(force/mass_e)
                        if p.y > screen_height + too_far:
                            p.y = screen_height - 2
                        if screen_height < p.y < screen_height + too_far:
                            force = p.force_between(p.x,p.x,p.y,screen_height,p.charge,wall_charge,1.0)
                            p.speed_y += -abs(force/mass_e)
                            
                    if p.y != 0:
                        if p.y < screen_height/2:
                            force = p.force_between(p.x,p.x,p.y,0,p.charge,wall_charge,1.0)
                            p.speed_y += -abs(force/mass_e)
                        if p.y <-too_far:
                            p.y = 2
                        if 0 > p.y > -too_far:
                            force = p.force_between(p.x,p.x,p.y,0,p.charge,wall_charge,1.0)
                            p.speed_y += abs(force/mass_e)

                            
                if no_walls == True:
                    if p.x < 0:
                        p.x = side_bar
                    if p.x > side_bar:
                        p.x = 0
                    if p.y > screen_height:
                        p.y = 1
                    if p.y < 0:
                        p.y = screen_height -1
                
                p.x += p.speed_x
                p.y += p.speed_y
                
                                
        if click_delay == 3:
            click_delay = 0
        if click_delay > 0:
            click_delay+=1
            
        if no_walls == False:
            pygame.draw.rect(display, light_blue,[side_bar-1, 0, 2, screen_height])
            pygame.draw.rect(display, light_blue,[0, 0, 2, screen_height])
            pygame.draw.rect(display, light_blue,[0, 0, screen_width, 2])
            pygame.draw.rect(display, light_blue,[0, screen_height - 2, screen_width, 2])
            
        pygame.draw.rect(display, light_grey,[side_bar, 0, 200, screen_height])            
        pygame.draw.rect(display, dark_grey,[side_bar, 0, 200, new_e_button_height])
        pygame.draw.rect(display, dark_grey,[side_bar, walls_button_y, 200, new_e_button_height])
        pygame.draw.rect(display, red,[side_bar, new_positron_y, 500, new_e_button_height])

        pygame.draw.rect(display, green ,[side_bar, bring_back_button_y, 200, new_e_button_height])
        
        pygame.draw.rect(display, dark_grey,[side_bar, speed_y_0_box, 200, new_e_button_height])
        message_diplay(side_bar+ 19, 10 ,"Add e", 14, white)
        message_diplay(side_bar+ 19, bring_back_button_y+10 ,"bring", 14, white)
        message_diplay(side_bar+ 19, bring_back_button_y+22 ,"back", 14, white)
        message_diplay(side_bar+ 19, new_positron_y+10 ,"Add p", 14, white)
        message_diplay(side_bar+ 19, new_positron_y+22 ,str(number_of_positrons), 14, white)
        message_diplay(side_bar+ 20, 22 ,str(number_of_electrons), 15, white)
        message_diplay(side_bar+ 20, speed_y_0_box + 22 ,"speed=0", 10, white)
        pygame.draw.rect(display, red,[side_bar, clear_button_y, 500, new_e_button_height])
        message_diplay(side_bar + 20, clear_button_y+20,"clear", 15, white)
        if no_walls == False:
            message_diplay(side_bar+ 20, walls_button_y+15 ,"remove ", 11, red)
            message_diplay(side_bar+ 20, walls_button_y+23 ,"walls ", 11, red)
            pygame.draw.rect(display, light_blue,[side_bar,wall_charge_button, screen_width, new_e_button_height])
            message_diplay(side_bar+ 20, wall_charge_button+12 ,"charge", 11, black)
            message_diplay(side_bar+ 14, wall_charge_button+23 ,"=", 11, black)
            message_diplay(side_bar+ 30, wall_charge_button+23 ,str(wall_charge), 11, black)
        if no_walls == True:
            message_diplay(side_bar+ 20, walls_button_y+8 ,"add", 11, red)
            message_diplay(side_bar+ 20, walls_button_y+15 ,"charged", 11, red)
            message_diplay(side_bar+ 20, walls_button_y+23 ,"  edges", 11, red)
        if choose_new_wall_charge==True:
            message_diplay(screen_width/2, walls_button_y+15 ,"type a number to choose wall charge", 18, black)
            
       
        
        pygame.display.update()
        clock.tick(200)

simulation()
pygame.quit()
quit()
