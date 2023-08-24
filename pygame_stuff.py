import pygame
from pygame import *
import math
import numpy as np
import random
from particles import electron, positron , e , wall_charge

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

new_positron_y = screen_height *0.8
speed_y_0_box = screen_height*0.5
side_bar = screen_width*0.95
new_e_button_height = screen_height*0.05
wall_charge_button = screen_height*0.4
clear_button_y = screen_height*0.95
walls_button_y = screen_height*0.3
bring_back_button_y = screen_height * 0.1
bring_back_y =  bring_back_button_y

def initialize():
    pygame.init()
    display = pygame.display.set_mode((int(screen_width), int(screen_height)))
    pygame.display.set_caption('electron simulator')
    clock = pygame.time.Clock()
    return display, clock

def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface, textSurface.get_rect()

def message_display(display , x,y, text, size,colour):
    largetext = pygame.font.Font('freesansbold.ttf', size) # make it large give it a font
    TextSurf, TextRect = text_objects(text, largetext,colour)       # pygame basically makes a textbox for text
    TextRect.center  = (x,y)
    display.blit(TextSurf, TextRect)

def write_id_num(id, display, x , y ):
    message_display(display , x,y, str(id),15,black)


def event_handle( new_electron , new_positron , choose_new_wall_charge , click_delay, electrons, positrons  , display, number_of_electrons , number_of_positrons , no_walls):
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
                    electrons.append(electron(mouse[0],mouse[1],e,0,0,number_of_electrons , yellow , len(electrons)))

        if new_positron == True:
            if mouse[0]<side_bar:
                if click[0] == True and click_delay == 0:
                    click_delay+=1
                    new_positron = False
                    number_of_positrons+=1
                    positrons.append(positron(mouse[0],mouse[1],-e,0,0,number_of_positrons , red , len(positrons)))
        if click_delay != 0:
            print(str(click_delay)+ "             click_delay   ")
        if mouse[0] > side_bar and mouse[1]<new_e_button_height:
    #        print("click for new e")
            if click[0] == True and click_delay == 0:
                new_electron = True
                click_delay+=5
                print("carrying  new e")
        #        time.sleep(5)
        if mouse[0] > side_bar and mouse[1]>clear_button_y:
            print("click to clear ")
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

#        if mouse[0] > side_bar and bring_back_y<mouse[1]<bring_back_y +new_e_button_height:
 #           if click[0] == True and click_delay == 0:
  #              click_delay+=1
   #             for i in electrons:
    #                if i.x > side_bar:
     #                   i.x = random.randint(screen_width*0.2,screen_width*0.8)
      #              if i.x < 0:
       ##                 i.x = random.randint(screen_width*0.2,screen_width*0.8)
         #           if i.y > screen_height:
          ##              i.y = random.randint(screen_height*0.2,screen_height*0.8)
            #        if i.y < 0:
             #           i.y = random.randint(screen_height*0.2,screen_height*0.8)
              #  for i in positrons:
               #     if i.x > side_bar:
                #        i.x = random.randint(screen_width*0.2,screen_width*0.8)
                 #   if i.x < 0:
                  #      i.x = random.randint(screen_width*0.2,screen_width*0.8)
                   # if i.y > screen_height:
     #                   i.y = random.randint(screen_height*0.2,screen_height*0.8)
      #              if i.y < 0:
       #                 i.y = random.randint(screen_height*0.2,screen_height*0.8)
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
    return new_electron, new_positron, click_delay , electrons , positrons, no_walls , choose_new_wall_charge , wall_charge

def draw_ui_n_walls(no_walls , choose_new_wall_charge , number_of_positrons , number_of_electrons , display):
            if no_walls == False:
                pygame.draw.rect(display, light_blue,[side_bar-2, 0, 4, screen_height])
                pygame.draw.rect(display, light_blue,[0, 0, 4, screen_height])
                pygame.draw.rect(display, light_blue,[0, 0, screen_width, 4])
                pygame.draw.rect(display, light_blue,[0, screen_height - 2, screen_width, 6])

            pygame.draw.rect(display, light_grey,[side_bar, 0, 200, screen_height])
            pygame.draw.rect(display, dark_grey,[side_bar, 0, 200, new_e_button_height])
            pygame.draw.rect(display, dark_grey,[side_bar, walls_button_y, 200, new_e_button_height])
            pygame.draw.rect(display, red,[side_bar, new_positron_y, 500, new_e_button_height])

#            pygame.draw.rect(display, green ,[side_bar, bring_back_button_y, 200, new_e_button_height])

            pygame.draw.rect(display, dark_grey,[side_bar, speed_y_0_box, 200, new_e_button_height])
            message_display(display ,side_bar+ 19, 10 ,"Add e", 14, white)
 #           message_display(display ,side_bar+ 19, bring_back_button_y+10 ,"bring", 14, white)
  #          message_display(display ,side_bar+ 19, bring_back_button_y+22 ,"back", 14, white)
            message_display(display ,side_bar+ 19, new_positron_y+10 ,"Add p", 14, white)
            message_display(display ,side_bar+ 19, new_positron_y+22 ,str(number_of_positrons), 14, white)
            message_display(display ,side_bar+ 20, 22 ,str(number_of_electrons), 15, white)
            message_display(display ,side_bar+ 20, speed_y_0_box + 22 ,"speed=0", 10, white)
            pygame.draw.rect(display, red,[side_bar, clear_button_y, 500, new_e_button_height])
            message_display(display ,side_bar + 20, clear_button_y+20,"clear", 15, white)
            if no_walls == False:
                message_display(display ,side_bar+ 20, walls_button_y+15 ,"remove ", 11, red)
                message_display(display ,side_bar+ 20, walls_button_y+23 ,"walls ", 11, red)
                pygame.draw.rect(display, light_blue,[side_bar,wall_charge_button, screen_width, new_e_button_height])
                message_display(display ,side_bar+ 20, wall_charge_button+12 ,"charge", 11, black)
                message_display(display ,side_bar+ 14, wall_charge_button+23 ,"=", 11, black)
                message_display(display ,side_bar+ 30, wall_charge_button+23 ,str(wall_charge), 11, black)
            if no_walls == True:
                message_display(display ,side_bar+ 20, walls_button_y+8 ,"add", 11, red)
                message_display(display ,side_bar+ 20, walls_button_y+15 ,"repelling", 11, red)
                message_display(display ,side_bar+ 20, walls_button_y+23 ,"  walls", 11, red)
            if choose_new_wall_charge==True:
                message_display(display ,screen_width/2, walls_button_y+15 ,"type a number to choose wall charge", 18, black)
