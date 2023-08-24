#     yellow, red , side_bar, screen_height

import pygame
import math
import time 
e = -10.0
y_list_ticker=0
mass_e = 0.0002
too_far = 400
wall_charge = -1.0
charge_constant = 50.0


class electron():
    def __init__(self,x,y,charge,speed_x,speed_y,electron_number , colour , thisid):
        self.x = x
        self.y = y
        self.charge = charge
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.num = electron_number
        self.colour = colour
        self.id = thisid

    def recieve_all_forces(self, electrons, positrons, no_walls, side_bar, screen_height):
        x_forces = []
        y_forces = []
        print(str(type(self))+ "   we are currrently     ++++++++++ ")
        for e in electrons:
            print(" lets start looking at e = " , e.id)
            if (e.id != self.id) or (e.charge != self.charge):
                print("starting to check force against an electron ")
                if self.y - e.y != 0:
                    theta = math.atan((self.x-e.x)/(self.y-e.y))
                else:
                    theta = 1
                force= self.force_between(self.x , e.x , self.y , e.y, self.charge, e.charge, charge_constant)

     #           x = force * math.cos(theta)
     #           y = force * math.sin(theta)
                print(force)
         #       if abs(force)>0.2:
          #          print(9/0)
                if force != 0:

                    dx = self.x - e.x
                    dy = self.y - e.y
                    if self.x > e.x and dy+dx != 0 :
                        print(str(self.speed_x)+ " self.speed_x   ere  1")
                        self.speed_x += (force/mass_e)*math.cos(theta) *(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft  1")
                    if self.x < e.x and dy+dx != 0:
                        print(str(self.speed_x)+ " self.speed_x   ere  2 ")
                        self.speed_x += -(force/mass_e)*math.cos(theta)*(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft 2 ")
                    if self.y > e.y and dy+dx != 0:
                        self.speed_y += (force/mass_e)*math.sin(theta)*(dy/(dy+dx))
                    if self.y < e.y and dy+dx != 0:
                        self.speed_y += -(force/mass_e)*math.sin(theta)*(dy/(dy+dx))
            else:
                print("neither (e.id != self.id) nor (e.charge != self.charge)   " , e.id , self.id ,e.charge , self.charge)
        for p in positrons:
            print(" lets start looking at p = " , p.id)
            if (p.id != self.id) or (p.charge != self.charge):
                print("starting to check force against a positron ")
                if self.y - p.y != 0:
                    theta = math.atan((self.x-p.x)/(self.y-p.y))
                else:
                    theta = 1
                force= self.force_between(self.x , p.x , self.y , p.y, self.charge, p.charge, charge_constant)
                print(force)
                if force != 0:

                    dx = self.x - p.x
                    dy = self.y - p.y
                    if self.x > p.x and dy+dx != 0 :
                        print(str(self.speed_x)+ " self.speed_x   ere  p1 ")
                        self.speed_x += (force/mass_e)*math.cos(theta) *(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft  p1")
                    if self.x < p.x and dy+dx != 0:
                        print(str(self.speed_x)+ " self.speed_x   ere  p2 ")
                        self.speed_x += -(force/mass_e)*math.cos(theta)*(dx/(dy+dx))
                        print(str(self.speed_x)+ " self.speed_x  aft  p2 ")
                    if self.y > p.y and dy+dx != 0:
                        self.speed_y += (force/mass_e)*math.sin(theta)*(dy/(dy+dx))
                    if self.y < p.y and dy+dx != 0:
                        self.speed_y += -(force/mass_e)*math.sin(theta)*(dy/(dy+dx))
            else:
                print("neither (p.id != self.id) nor (p.charge != self.charge)   " , p.id , self.id ,p.charge , self.charge)
                #### if there are walls around the edge, feel a force from them
        if no_walls == False:
            if 0<self.x < side_bar/2:
                force = float(self.force_between(self.x,0,self.y,self.y,self.charge,wall_charge,charge_constant))
                self.speed_x += abs(force/mass_e)
            if self.x < 0:  ### if were off screen
                self.x = 2.0
            if side_bar> self.x > side_bar/2:
                force = float(self.force_between(self.x,side_bar,self.y,self.y,self.charge,wall_charge,charge_constant))
                self.speed_x += -abs(force/mass_e)
            if self.x > side_bar :
                self.x = float(side_bar - 2.0)
            if screen_height > self.y > screen_height/2:
                force = self.force_between(self.x,self.x,self.y,screen_height,self.charge,wall_charge,charge_constant)
                self.speed_y += float(-abs(force/mass_e))
            if self.y > screen_height:
                self.y = float(screen_height - 2.0)
            if 0<self.y < screen_height/2:
                force = self.force_between(self.x,self.x,self.y,0,self.charge,wall_charge,charge_constant)
                if type(force) is None:
                    force = 0.0
                self.speed_y += float(abs(force/mass_e))
            if self.y < 0:
                self.y = 2.0
            

 #       print(str(self.speed_x)+ " self.speed_x ")
        if no_walls == False:
            does_this_get_past_barriers = self.does_this_move_past_barriers_next_frame([self.x + self.speed_x , self.y + self.speed_y], side_bar, screen_height)
            if does_this_get_past_barriers[0] != False:
                self.x = does_this_get_past_barriers[0]
                self.y = does_this_get_past_barriers[1]
            else:
                self.x += self.speed_x
                self.y += self.speed_y
        else:
            self.x += self.speed_x
            self.y += self.speed_y
#        time.sleep(1)
#        print("aight")

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
            print(" charge1 , charge2 " , charge1,charge2)
            print("force between  = charge1*charge2 / 4*pi*e_0 / r_len**2   =   " , charge1*charge2,' / ' , 4*pi*e_0  , ' / ' , r_len**2 , "   =   " , F)
            print(F)
            return(F)


    def draw(self , display):
        pygame.draw.circle(display, self.colour,(int(self.x), int(self.y)), 6,6)


    def position_manager(self , no_walls , side_bar , screen_height):


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
    
    def does_this_move_past_barriers_next_frame(self, next_pos, side_bar, screen_height):
        if next_pos[0] < 0.00001 and (screen_height > next_pos[1] > 0.00001): # if just off left edge
            return [1, next_pos[1]]
        elif (side_bar > next_pos[0] > 0.00001) and (next_pos[1] < 0.00001): # if just off top edge
            return [next_pos[0] , 1]
        elif (next_pos[0] > side_bar-0.00001) and (screen_height > next_pos[1] > 0.00001): # if just off right edge
            return [side_bar-1, next_pos[1]]
        elif (side_bar > next_pos[0] > 0.00001) and (next_pos[1] > screen_height): # if just off bottom edge
            return [next_pos[0] , screen_height-1]
        elif next_pos[0] < 0.00001 and (next_pos[1] < 0.00001): # if off top left
            return [1, 1]
        elif next_pos[0] > side_bar - 0.00001 and (next_pos[1] < 0.00001): # if off top right
            return [side_bar - 1, 1]
        elif next_pos[0] > side_bar - 0.00001 and (next_pos[1] > screen_height - 0.00001): # if off bottom right
            return [side_bar - 1, screen_height - 1]
        elif next_pos[0] < 0.00001 and (next_pos[1] > screen_height - 0.00001): # if off bottom left
            return [1, screen_height - 1]
        else:
            return [False, False]

class positron(electron):
    def __init__(self,x,y,charge,speed_x,speed_y,electron_number , colour , thisid):
        self.x = x
        self.y = y
        self.charge = charge
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.num = electron_number
        self.colour = colour
        self.id = thisid