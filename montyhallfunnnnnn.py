from random import seed
from random import randint
import array as arr
a = 0
b = 0
c = 0
t = a + b + c
g = arr.array('i', [])
def Montyhall():
    global a
    global b
    global c
    global t
    global g
    g = arr.array('i', [])
    while t != 2:
        a = randint(0, 1)
        b = randint(0, 1)
        c = randint(0, 1)
        t = a + b + c
    g.append(a)
    g.append(b)
    g.append(c)
    global player_choice
    player_choice = randint(0, 2)
    global p
    p = player_choice
    player_choice = g[player_choice]
    opened_door()
def opened_door():
    global a
    global b
    global c
    global t
    global g
    global p
    global j
    global player_choice
    rep_choice = randint(0, 2)
    r = rep_choice
    rep_choice = g[rep_choice]
    while (r == p or rep_choice == 0):
        rep_choice = randint(0, 2)
        r = rep_choice
        rep_choice = g[rep_choice]
    g.pop(r)
    checking()
def checking():
    global p
    global j
    global g
    global l
    global player_choice
    if(player_choice==0):
        l=l+1
    else :
        j=j+1
i=0
l=0
j=0
while i<1000000:
    Montyhall()
    i+=1
j=j/i
l=l/i
print("the times you won when changing :",j)
print("the times you won without changing :",l)
