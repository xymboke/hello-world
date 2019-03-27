from turtle import*
speed(6)
pensize(5)
r = 47
color = ['blue','black','red','yellow','green']
posx = [-100,0,100,-60,60]
posy = [-20,-20,-20,-70,-70]
for i in range(5):
    pencolor(color.pop())
    penup()
    goto(posx.pop(),posy.pop())
    pendown()
    circle(r)



































    
    
'''
from turtle import*
speed(4)
pensize(2)
color=["red","blue","yellow","pink","gray"]
for x in range(5):
    pencolor(color[x%5])
    if x==3:
        home()
        goto(50,-50)
        
    pendown()
    circle(50)
    penup()
    forward(100)


'''
