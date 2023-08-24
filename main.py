from pygame_stuff import *
from particles import *

###### to do 
### just replace number_of_electrons , number_of_positrons with len electrons
### change e variable to charge
### change to non linear acceleration to fix a bunch of problems
### 

def simulation():
    display, clock = initialize()
    click_delay = 0

    number_of_electrons = 0
    number_of_positrons = 0

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
        electrons.append(electron(x,y,e,0.0,0.0,i, yellow , len(electrons)))
          #(self,x,y,charge,speed_x,speed_y,electron_number):
    for p in range(number_of_positrons):
        x=(random.uniform(0,screen_width))
        y=(random.uniform(0,screen_height))
        positrons.append(positron(x,y,-e,0.0,0.0,i , red  , len(positrons)))

    quit_bool = False
    while quit_bool == False:

        display.fill(white)
        draw_ui_n_walls(no_walls, choose_new_wall_charge , number_of_positrons , number_of_electrons  , display)
                                                                                   #( new_electron , new_positron , choose_new_wall_charge , click_delay, electrons, positrons  , display, number_of_electrons , number_of_positrons , no_walls)
        new_electron, new_positron, click_delay , electrons , positrons, no_walls , choose_new_wall_charge, particles.wall_charge = event_handle( new_electron , new_positron , choose_new_wall_charge , click_delay , electrons, positrons , display , number_of_electrons , number_of_positrons , no_walls)
        
        for i in electrons:
            #recieve_all_forces(self, electrons, positrons, no_walls)
            i.recieve_all_forces(electrons, positrons, no_walls , side_bar, screen_height)
            i.position_manager(no_walls  , side_bar , screen_height)
            i.draw(display)
            write_id_num(i.id , display, i.x , i.y)

        for p in positrons:
            p.recieve_all_forces(electrons, positrons, no_walls , side_bar, screen_height)
            p.position_manager(no_walls  , side_bar , screen_height)
            p.draw(display)
            write_id_num(p.id, display, p.x , p.y)


        if click_delay == 5:
            click_delay = 0
        if click_delay > 0:
            click_delay+=1

        pygame.display.update()
        clock.tick(20)
 #       if (len(electrons) + len(positrons)) >1:
  #          raise Exception("  ggggg  ")
     #   print("uno")
      #  time.sleep(120)
      #  time.sleep(5)

    pygame.quit()
    sys.exit()


simulation()
pygame.quit()
quit()