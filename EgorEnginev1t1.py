'''Module code'''
from tkinter import * #подключение модуля
from threading import Thread
import time
import playsound

'''Module code is end'''


def begin(**kwargs): #начальная функция
    sizeofroot = kwargs['size']
    widthroot = ''
    heightroot = ''
    width_end = False
    for i in sizeofroot:
        if i == '*':
            width_end = True
        else:
            
           if width_end != True:
               widthroot += i
           else:
               heightroot += i
        
            
    print(widthroot, heightroot)       
    global root, c, time
    import time
    root = Tk() #создание окна и холста
    c = Canvas(root, bg = 'white', width = int(widthroot), height = int(heightroot))
    
'''Normal code'''


'''MUSIC ENGINE PART'''
def uploadwav(**kwargs):
    
    dictmusic[kwargs['name']] = kwargs['media']
    return dictmusic
def playwav_inthread(**kwargs):
    
    playsound.playsound(dictmusic[kwargs['name']])
    return True
    
def playwav(**kwargs):
    
    thr = Thread(target = lambda: playwav_inthread(**kwargs))
    thr.start()
    return True
    
    
def playwavloop(**kwargs):
    playwav(**kwargs)
    root.after(kwargs['after'], lambda: playwavloop(**kwargs))
        
        
    



'''PHYSICS ENGINE PART'''
global root, c, time, dictnms, funa, v, arrcoll, objects_side, blocked_obj, arrnms, dictmusic
v = 5

dictnms = {} #создание словаря для хранения имен геом. фигур
objects_side = {}
arrnms = []
arrcoll = {}
blocked_obj = []
dictmusic = {}
def creat_obj(**kwargs): #создание геом. фигур
    x1 = kwargs['x1']
    y1 = kwargs['y1']
    x2 = kwargs['x2']
    y2 = kwargs['y2']
    name = kwargs['name']
    color = kwargs['color']
    figure = kwargs['figure']
    if name in dictnms:
        print('Object with this tag already create')
    else:
        if figure == 'rect' or figure == 'rectangle':#создание квадрата
            c.create_rectangle(x1,y1,x2,y2,fill = color, tag = name)
        
            name = name
            dictnms[name] = [x1, y1, x2, y2]
            arrnms.append(name)
        elif figure == 'oval':#создание окружности
            c.create_oval(x1, y1, x2, y2, fill = color, tag = name)
    #return x1, y1, x2, y2, name, color, figure
def collide(**kwargs): # nameofobject, type    Обработчик столкновений
    #print('gjfdig')
    name = kwargs['name']
    name2 = kwargs['name2']
    
    
   
    if dictnms[name][0] + v >= dictnms[name2][0] and dictnms[name][1] + v >= dictnms[name2][1] and dictnms[name][2] - v <= dictnms[name2][2] and dictnms[name][3] - v <= dictnms[name2][3]:
        
        
        
        
        if objects_side['hero'] == 'jump':
           move(name = 'hero', side = objects_side['hero'], intervalx = -10, intervaly = -10)
           return True
        try:
           move(name = 'hero', side = objects_side['hero'], intervalx = -5, intervaly = -5) #ground()
        except:
            pass
        
        return True
 
    
      
      
          

    return False
    
def move(**kwargs):#передвижение созданных геом. фигур
    #print(arrcoll, arrnms)
    side = kwargs['side']
    name = kwargs['name']
    intervalx = kwargs['intervalx']
    intervaly = kwargs['intervaly']
    
    try:
        
       blocked = kwargs['blocked']
    except:
       blocked = None
   
    objects_side[kwargs['name']] = kwargs['side']
    
    if name in blocked_obj:
        blocked = objects_side[kwargs['name']]
    time.sleep(0.001) #плавная отрисовка
    if side == 'right' and blocked != 'right':
        if intervalx == 0:
            print('MoveWarning, interval is equal to Zero!!!')
       
        c.coords(name, dictnms[name][0] + intervalx, dictnms[name][1] , dictnms[name][2]  + intervalx, dictnms[name][3] )
        dictnms[name][0] = dictnms[name][0] + intervalx 
        dictnms[name][2] = dictnms[name][2] + intervalx 
        
        
    
    elif side == 'down' and blocked != 'down':
        if intervaly == 0:
            print('MoveWarning, interval is equal to Zero!!!')
        
        c.coords(name, dictnms[name][0], dictnms[name][1] + intervaly , dictnms[name][2], dictnms[name][3] + intervaly)
        dictnms[name][1] = dictnms[name][1] + intervaly
        dictnms[name][3] = dictnms[name][3] + intervaly
        
    elif side == 'left' and blocked != 'left':
        if intervalx == 0:
            print('MoveWarning, interval is equal to Zero!!!')
        
        c.coords(name, dictnms[name][0] - intervalx, dictnms[name][1] , dictnms[name][2]  - intervalx, dictnms[name][3] )
        dictnms[name][0] = dictnms[name][0] - intervalx 
        dictnms[name][2] = dictnms[name][2] - intervalx 
        
        
        
    elif side == 'up' and blocked != 'up':
        if intervaly == 0:
            print('MoveWarning, interval is equal to Zero!!!')
        
        
        c.coords(name, dictnms[name][0], dictnms[name][1] - intervaly , dictnms[name][2], dictnms[name][3] - intervaly)
        dictnms[name][1] = dictnms[name][1] - intervaly 
        dictnms[name][3] = dictnms[name][3] - intervaly 
        
    
              
    else:
        
        print('Unknown side({})'.format(side))
    kwargs['blocked'] = None
    return side, name, intervalx, intervaly

def KeyPressFunc(event, PressKey, funcname, kwargs):#обработка внешних событий с клавиатуры
    #print(dictnms)
    
    if funcname in globals():
        
        func = globals()[funcname]
        func(**kwargs)
    else:
        
        func = lambda event: funcname(event)
        func(event)

    
    
          
   
    

    
    
    #collide(**kwargs)
    
    
    
def KeyPress(funcname, PressKey, **kwargs):#распознавание внешних событий с клавиатуры
    
    root.bind(PressKey, lambda event: KeyPressFunc(event, PressKey, funcname, kwargs))
def all_coll(**kwargs):
    
    for i in range(len(arrnms)):
        for j in range(len(arrnms)):
            
            if i == j:
                pass
            else:
                
               name = arrnms[i]
               name2 = arrnms[j]
               if collide(name = name, name2 = name2) == True:
                   arrcoll[name] = name2
                   
               
    if dictnms['hero'][1] < 60:
        move_all('down')
    elif dictnms['hero'][3] > 300:
        move_all('up')
    elif dictnms['hero'][0] < 80:
        move_all('right')
    elif dictnms['hero'][2] > 150:
        move_all('left')
    root.after(1, lambda: all_coll(**kwargs))
def coll_del(name):
    
        
        
    del(arrcoll[name])
def move_all(side):
    for i in dictnms:
        move(name = i, intervalx = 5, intervaly = 5, side = side)
def gravity(**kwargs):
    
    
        
    move(name = kwargs['name'], side = 'down', intervalx = 0, intervaly = kwargs['power'])
    root.after(80, lambda: gravity(**kwargs))
def runafter():
    return root

def end(*args):
    
    
    c.pack()#конец
    
    root.mainloop()

'''PHYSICS ENGINE PART IS END'''



    

            
        
                
