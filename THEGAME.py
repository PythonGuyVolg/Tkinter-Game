'''Module code'''
from EgorEnginev1t1 import *
import random
'''Module code is end'''

musicFile1 = 'EarthSound.mp3'
musicFile2= 'Doom-E1M1_SC-8850.mp3'
arr = [['1','0','0','0','0','0','0','0','0','0'],   #Game map( changeable )
      ['0','1','1','0','0','0','0','0','1','1'],    # 1 - ground, 0 - air, 2 - 'hero'
      ['0','0', '0','1','0','1','1','1','0','0', '1'],
      ['0','0','1','1','1','0','0','0','0','1', '1'],
      ['1','0','0','0','0','1','1','0','1','0'],
      ['0','1','0','','0','0','0','1','0','1'],
      ['0','0','1','0','0','0','1','0','0','0'],
      ['0','1','0','1','0','2','0','1','1','0'],
      ['1','1','1','1','1','1','1','1','1','1'],]

def map_read(array, v):  #reading map array and creating level
    x1 = 0
    x2 = 0
    y1 = 0
    y2= 15
    for i in range(len(array)):
        y1 += 30
        y2 += 30
        x1 = 5
        x2 = 30
        for j in range(len(array)):

           
           x1 += 25
           x2 += 25
           
           if array[i][j] == '0':
              x1 += 0
              x2 += 0
              
           if array[i][j] == '1':
             
             
             creat_obj(x1 = x1 , y1 = y1, x2 = x2, y2 = y2, name = 'add{}'.format(random.randint(0, 10000000)), color = 'orange', figure = 'rect')
           if array[i][j] == '2':
               creat_obj(x1 = x1 , y1 = y1, x2 = x2 - 15, y2 = y2 - 5, name = 'hero', color = 'green', figure = 'rect')

        
    #print(objects_side)     
def ground():   #  play music when 'hero' on the ground
    
    
    if 'hero' in arrcoll: # if 'hero' have collision with any object
        uploadwav(media = musicFile1, name = 'run_ground') #Upload file with music(wav or mp3)
        playwav(name = 'run_ground') # play music
        coll_del('hero') # delete 'hero' in array with all collisions in the game
    runafter().after(500, ground)

def jump(event, **kwargs): # jump function
    
    if 'hero' in arrcoll: #if 'hero' have collision with any object
    
        
        
            
        move(name = 'hero', side = 'up', intervaly = 5, intervalx = 0) # jump
        
        runafter().after(20, lambda: jump(event, **kwargs))
        
    
begin(size = '1000*720') # begin mainloop
map_read(arr, 40) # read game map
'''Debug code'''
#creat_obj(x1 = 20, y1 = 35, x2 = 30, y2 = 45, name = 'hero', color = 'green', figure = 'rect')
#creat_obj(x1 = 160, y1 = 80, x2 = 240, y2 = 120, name = 'evil2', color = 'black', figure = 'rect')
#creat_obj(x1 = 0, y1 = 200,x2 = 200, y2 = 250, name = 'evil', color = 'brown', figure = 'rect')
#creat_obj(x1 = 40, y1 = 40,x2 =  60, y2 = 60, name = 'evil3', color = 'black', figure = 'rect')
#creat_obj(x1 = 0, y1 = 0, x2 = 800, y2 = 0, name = 'platf', color = 'brown', figure = 'rect')
#creat_obj(x1 = 200, y1 = 500, x2 = 400, y2 = 550, name = 'platf2', color = 'brown', figure = 'rect')
#gravity(name = 'evil2', power = 1)
'''Debug code'''
KeyPress('creat_obj', 'g', x1 = 20, y1 = 35, x2 = 30, y2 = 45, name = 'hero', color = 'black', figure = 'rect') #Keypress(func, key_name, **kwargs)
KeyPress('move', 'd', name = 'hero', side = 'right', intervalx = 5, intervaly = 0)
KeyPress('move', 's', name = 'hero', side = 'down', intervalx = 0, intervaly = 5)
KeyPress(jump, '<Key-space>', name = 'hero')
KeyPress('move', 'w', name = 'hero', side = 'up', intervalx = 0, intervaly = 5)
KeyPress('move', 'a', name = 'hero', side = 'left', intervalx = 5, intervaly = 0)
all_coll()
gravity(name = 'hero', power = 5) # Gravity for 'hero'


uploadwav(media = musicFile2, name = 'DOOM') # upload DOOM music :)  

playwav(name = 'DOOM') #play DOOM music

ground() 

end() # end.
