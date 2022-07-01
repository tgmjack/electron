import pygame
from pygame import *
import math
import numpy as np
import random
import time
## to do list
# fix quit error
# frame rate controls
# fix up actual gauss
# tidy up
# ,=make build 

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
        self.colour = yellow

    def recieve_all_forces(self, electrons, positrons, no_walls):
        x_forces = []
        y_forces = []
        print(str(type(self))+ "   we are currrently ")
        for e in electrons:
            if e != self:
                print("theres this e ")
                if self.y - e.y != 0:
                    theta = math.atan((self.x-e.x)/(self.y-e.y))
                else:
                    theta = 1
                force= self.force_between(self.x , e.x , self.y , e.y, self.charge, e.charge, 1.0)
    #            x = force * math.cos(theta)
     #           y = force * math.sin(theta)
                print(force)
                if force != 0:
                    
                    dx = self.x - e.x              
                    dy = self.y - e.y
                    if self.x > e.x and dy+dx != 0 :
                        print(str(self.speed_x)+ " self.speed_x   ere ")
                        self.speed_x += abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft")
                    if self.x < e.x and dy+dx != 0:
                        print(str(self.speed_x)+ " self.speed_x   ere ")
                        self.speed_x += -abs((force/mass_e)*math.cos(theta))*(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft")
                    if self.y > e.y and dy+dx != 0:
                        self.speed_y += abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                    if self.y < e.y and dy+dx != 0:
                        self.speed_y += -abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))

        for p in positrons:
            if p != self:
                print("theres this p ")
                if self.y - p.y != 0:
                    theta = math.atan((self.x-p.x)/(self.y-p.y))
                else:
                    theta = 1
                force= self.force_between(self.x , p.x , self.y , p.y, self.charge, p.charge, 1.0)
    #            x = force * math.cos(theta)
     #           y = force * math.sin(theta)
                print(force)
                if force != 0:
                    
                    dx = self.x - p.x              
                    dy = self.y - p.y
                    if self.x > p.x and dy+dx != 0 :
                        print(str(self.speed_x)+ " self.speed_x   ere ")
                        self.speed_x += abs((force/mass_e)*math.cos(theta)) *(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft")
                    if self.x < p.x and dy+dx != 0:
                        print(str(self.speed_x)+ " self.speed_x   ere ")
                        self.speed_x += -abs((force/mass_e)*math.cos(theta))*(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft")
                    if self.y > p.y and dy+dx != 0:
                        self.speed_y += abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))
                    if self.y < p.y and dy+dx != 0:
                        self.speed_y += -abs((force/mass_e)*math.sin(theta))*(dy/(dy+dx))

                #### if there are walls around the edge, feel a force from them
        if no_walls == False:
            if 0<self.x < side_bar/2:
                force = float(self.force_between(self.x,0,self.y,self.y,self.charge,wall_charge,1.0))
                self.speed_x += abs(force/mass_e)
            if self.x < 0:  ### if were off screen
                self.x = 2.0
            if side_bar> i.x > side_bar/2:
                force = float(self.force_between(self.x,side_bar,self.y,self.y,self.charge,wall_charge,1.0))
                self.speed_x += -abs(force/mass_e)
            if self.x > side_bar :
                self.x = float(side_bar - 2.0)
            if screen_height > self.y > screen_height/2:
                force = self.force_between(self.x,self.x,self.y,screen_height,self.charge,wall_charge,1.0)
                self.speed_y += float(-abs(force/mass_e))
            if self.y > screen_height:
                self.y = float(screen_height - 2.0)
            if 0<self.y < screen_height/2:
                force = self.force_between(self.x,self.x,self.y,0,self.charge,wall_charge,1.0)
                if type(force) is None:
                    force = 0.0
                self.speed_y += float(abs(force/mass_e))
            if self.y < 0:
                self.y = 2.0

        print(str(self.speed_x)+ " self.speed_x ")
        self.x += self.speed_x
        self.y += self.speed_y
        print("aight")

    #    if i.y < 1:
    #        i.y = screen_height



    def force_between(self,x1,x2,y1,y2,charge1,charge2,e_0):
        x = x1-x2
        y = y1-y2
        r_len = ((x**2)+(y**2))**0.5
        pi = 3.14159265358987
        if r_len == 0:
            return 0
        else:
            F = ((charge1*charge2)/(4*pi*e_0))/(r_len**2)
            return(F)


    def draw(self):
        pygame.draw.circle(display, self.colour,(int(self.x), int(self.y)), 6,6)

    def position_manager(self , no_walls):

        maybe_old_crap = """
        if no_walls == True:  ## ie ) if we go off the lerft side of screeen we should re enter from the right and vice versa
            if i.x>side_bar-1 and i.speed_x > 0:
                i.x = 0.0
            if  i.x<1 and i.speed_x < 0:
                i.x = float(side_bar-1 )
            if  i.y>screen_height-2 and i.speed_y > 0:
                i.y = 0.0
            if  i.y<1 and i.speed_y < 0:
                i.y = float(screen_height)  """
        
         ## ie ) if we go off the lerft side of screeen we should re enter from the right and vice versa
        if no_walls == True:
            if self.x < 0:
                self.x = side_bar
            if self.x > side_bar:
                self.x = 0
            if self.y > screen_height:
                self.y = 1
            if self.y < 0:
                self.y = screen_height -1

class positron(electron):
    def __init__(self,x,y,charge,speed_x,speed_y,electron_number):
        self.x = x
        self.y = y
        self.charge = charge
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.num = electron_number
        self.colour = red

def event_handle( new_electron , new_positron , choose_new_wall_charge , click_delay):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            a = 11
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if new_electron == True:
            print("new electron true ")
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
        print(str(click_delay)+ "             click_delay   ")
        if mouse[0] > side_bar and mouse[1]<new_e_button_height:
            print("click for new e")
            if click[0] == True and click_delay == 0:
                new_electron = True
                click_delay+=1
                print("carrying  new e")
                time.sleep(5)
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
########## draw arrows to indicate next click creates particle
        if new_electron == True and mouse[0]<side_bar:
            pygame.draw.line(display, yellow,(mouse[0]-7,mouse[1]-7),(mouse[0]+7,mouse[1]+7),3) #
            pygame.draw.line(display, yellow,(mouse[0]-7,mouse[1]+7),(mouse[0]+7,mouse[1]-7),3)
        if new_positron == True and mouse[0]<side_bar:
            pygame.draw.line(display, red,(mouse[0]-7,mouse[1]-7),(mouse[0]+7,mouse[1]+7),3) #
            pygame.draw.line(display, red,(mouse[0]-7,mouse[1]+7),(mouse[0]+7,mouse[1]-7),3)


def draw_ui_n_walls(no_walls , choose_new_wall_charge , number_of_positrons , number_of_electrons):
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



new_positron_y = screen_height *0.8
speed_y_0_box = screen_height*0.5
side_bar = screen_width*0.95
new_e_button_height = screen_height*0.05
wall_charge_button = screen_height*0.4
clear_button_y = screen_height*0.95
walls_button_y = screen_height*0.3
bring_back_button_y = screen_height * 0.1
bring_back_y =  bring_back_button_y





e = -10.0
y_list_ticker=0
mass_e = 0.0002
too_far = 400
wall_charge = -1.0



def simulation():
    click_delay = 0

    number_of_electrons = 3
    number_of_positrons = 3
    
    new_electron = False
    new_positron = False
    choose_new_wall_charge = False
    no_walls = True    

####### this section creates initial particles in an evenly disributed grid
    electrons = []
    positrons = []

    for i in range(number_of_electrons):
        x=(random.uniform(0,screen_width))
        y=(random.uniform(0,screen_height))
        electrons.append(electron(x,y,e,0.0,0.0,i))
          #(self,x,y,charge,speed_x,speed_y,electron_number):
    for p in range(number_of_positrons):
        x=(random.uniform(0,screen_width))
        y=(random.uniform(0,screen_height))
        positrons.append(positron(x,y,-e,0.0,0.0,i))
    quit_bool = False
    while quit_bool == False:

        display.fill(white)
        draw_ui_n_walls(no_walls, choose_new_wall_charge , number_of_positrons , number_of_electrons)
        event_handle( new_electron , new_positron , choose_new_wall_charge , click_delay)

        for i in electrons:
            #recieve_all_forces(self, electrons, positrons, no_walls)
            i.recieve_all_forces(electrons, positrons, no_walls)
            i.position_manager(no_walls)
            i.draw()

        for p in positrons:
            p.recieve_all_forces(electrons, positrons, no_walls)
            p.position_manager(no_walls)
            p.draw()


        if click_delay == 5:
            click_delay = 0
        if click_delay > 0:
            click_delay+=1

        pygame.display.update()
        clock.tick(20)
        print("uno")
      #  time.sleep(120)
      #  time.sleep(5)
        
    pygame.quit()
    sys.exit()


simulation()
pygame.quit()
quit()
