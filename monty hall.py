from random import seed
from random import randint
import array as arr

h=0
global a
global b
global c
global e
global j
global l
l=0
q=0
j=0

i=0


def funnn(s):
  global j
  global l
  if(s==g[0]):
    s=g[1]
  else:
    s=g[0]
  if(s==0):
    j=j+1
  else:
    l=l+1


def fun():

  if h==10:
    end()
  g.append(a)
  g.append(b)
  g.append(c)


  global s
  s=randint(0,2)
  global e
  e=s
  s=g[s]

  openss()

def openss():
  s1=0
  while(1):
    d=arr.array('i', [a, b, c])
    d=g
    s1 = randint(0, 2)
    r=s1
    s1 = d[s1]
    if s1!=0 and r!=e:
      d.remove(s1)

      break
    else :
      continue
  funnn(s)
def end():
  global j
  global i
  global l
  j=j/i
  l=l/i
  print("the times you won when switching :",j)
  print("the times you won without switching",l)
  name=input ("press any key to restart")

while (i<100):
  a = b = c = 0
  t = a + b + c
  global g
  g = arr.array('i', [])

  while t != 2:
    a = randint(0, 1)
    b = randint(0, 1)
    c = randint(0, 1)
    t = a + b + c
  fun()
  i+=1


end()
