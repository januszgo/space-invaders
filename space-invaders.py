# -*- coding: utf-8 -*-
import turtle
import math
import winsound
import time
import random
#Ekran główny
ekran=turtle.Screen()
ekran.title("Space Invaders 2019")
ekran.bgpic("space_invaders_background.gif")
#Ekran ładowania
turtle.register_shape("loading_background.gif")
turtle.register_shape
loadscreen=turtle.Turtle()
loadscreen.shape("loading_background.gif")
time.sleep(2)
loadscreen.hideturtle()
#Tablica wyników
wynik=25
life=5
level=1
wynik_tab=turtle.Turtle()
wynik_tab.speed(0)
wynik_tab.color("red")
wynik_tab.penup()
wynik_tab.setposition(-390,295)
wynik_str="Score: %s" %wynik
wynik_tab.write(wynik_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
wynik_tab.hideturtle()
#Tablica żyć
life_tab=turtle.Turtle()
life_tab.speed(0)
life_tab.color("red")
life_tab.penup()
life_tab.setposition(-230,295)
life_str="Health: %s" %life
life_tab.write(life_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
life_tab.hideturtle()
#Tablica poziomów
level_tab=turtle.Turtle()
level_tab.speed(0)
level_tab.color("red")
level_tab.penup()
level_tab.setposition(-70,295)
level_str="Level: %s" %level
level_tab.write(level_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
level_tab.hideturtle()
#Powiadomienia
news=turtle.Turtle()
news.speed(0)
news.color("white")
news.hideturtle()
news.penup()
news.setposition(60,295)
#Gracz
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("bullet1.gif")
turtle.register_shape("gift.gif")
turtle.register_shape("gift1.gif")
gracz=turtle.Turtle()
gracz.shape("player.gif")
gracz.speed(0)
gracz.penup()
gracz.setposition(0,-250)
vgracz=20
vprzeciwnik=2
#Przeciwnicy
enemies=5
przeciwnicy=[]
for i in range(enemies):
    przeciwnicy.append(turtle.Turtle())
for przeciwnik in przeciwnicy:
    przeciwnik.shape("enemy.gif")
    przeciwnik.speed(0)
    przeciwnik.penup()
    przeciwnik.setposition(random.randint(-250,250),random.randint(150,250))
#Pocisk
pocisk=turtle.Turtle()
pocisk.shape("bullet.gif")
pocisk.speed(0)
pocisk.penup()
pocisk.hideturtle()
vpocisk=30
#Pocisk przeciwnika
pocisk1=turtle.Turtle()
pocisk1.shape("bullet1.gif")
pocisk1.speed(0)
pocisk1.penup()
pocisk1.hideturtle()
vpocisk1=30
#spocisk: 1-gotowy 2-wystrzelony
spocisk=1
spocisk1=1
#Bonus
bonus=turtle.Turtle()
bonus.shape("gift.gif")
bonus.speed(0)
bonus.hideturtle()
bonus.penup()
bonus.setposition(400,400)
vbonus=10
sbonus=1
#Przesuwanie gracza
def wlewo():
    x=gracz.xcor()
    x-=vgracz
    if level==3:
        if x<-200:
            x=-200
    else:
        if x<-320:
            x=-320
    gracz.setx(x)
def wprawo():
    x=gracz.xcor()
    x+=vgracz
    if level==3:
        if x>200:
            x=200
    else:
        if x>320:
            x=320
    gracz.setx(x)
#Wystrzał
def strzelaj():
    global spocisk
    if spocisk==1:
        #winsound.PlaySound("shot1.wav", winsound.SND_ASYNC)
        spocisk=2
        pocisk.setposition(gracz.xcor(),gracz.ycor()+16)
        pocisk.showturtle()
#Wystrzał przeciwnika
def strzelaj1(x,y):
    global spocisk1
    #winsound.PlaySound("shot1.wav", winsound.SND_ASYNC)
    pocisk1.setposition(x,y-16)
    pocisk1.showturtle()
#Funkcja kończąca grę w razie wciśnięcia q
def koniec():
    global k
    k=0
#Wczytywanie klawiszy
turtle.listen()
turtle.onkey(wlewo,"Left")
turtle.onkey(wprawo,"Right")
turtle.onkey(strzelaj,"space")
turtle.onkey(koniec,"q")
k=1
t=0
x=0
c1=0
c2=0
punktacja=1
agresja=40
bonuscounter=0
licznik=0
#Mainloop
while 1:
    for przeciwnik in przeciwnicy:
        #Przesuwanie przeciwników
        przeciwnik.setx(przeciwnik.xcor()+vprzeciwnik)
        if level==3:
            if przeciwnik.xcor()>200 or przeciwnik.xcor()<-200:
                if licznik>30:
                    licznik=0
                    for i in przeciwnicy:
                        i.sety(i.ycor()-32)
                vprzeciwnik*=-1
                licznik+=1
        else:
            if przeciwnik.xcor()>320 or przeciwnik.xcor()<-320:
                for i in przeciwnicy:
                    i.sety(i.ycor()-32)
                vprzeciwnik*=-1
        #Przeciwnik strzela
        if spocisk1==1 and abs(gracz.xcor()-przeciwnik.xcor())<20: 
            if t>agresja:
                strzelaj1(przeciwnik.xcor(),przeciwnik.ycor())
                spocisk1=2
                t=0
            else:
                t+=1
        #Zastrzelenie przeciwnika
        if math.sqrt(math.pow(pocisk.xcor()-przeciwnik.xcor(),2)+math.pow(pocisk.ycor()-przeciwnik.ycor(),2))<20:
            #winsound.PlaySound("shot.wav", winsound.SND_ASYNC)
            pocisk.hideturtle()
            pocisk.setposition(-400,-400)
            if level==3:
                przeciwnik.setposition(random.randint(-150,150),random.randint(150,250))
            else:
                przeciwnik.setposition(random.randint(-250,250),random.randint(150,250))
            wynik+=1*punktacja
            if sbonus==1:
                bonuscounter+=1
            wynik_tab.clear()
            wynik_str="Score: %s" %wynik
            wynik_tab.write(wynik_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
            wynik_tab.hideturtle()
        #Zjedzenie gracza
        if math.sqrt(math.pow(gracz.xcor()-przeciwnik.xcor(),2)+math.pow(gracz.ycor()-przeciwnik.ycor(),2))<20:
            gracz.hideturtle()
            przeciwnik.hideturtle()
            k=0
    #Wysłanie bonusu
    if bonuscounter>3 and sbonus==1:
        x=random.randint(1,2)
        if x==1:
            bonus.shape("gift.gif")
        else:
            bonus.shape("gift1.gif")
        bonus.setposition(0,300)
        bonus.showturtle()
        bonuscounter=0
        sbonus=2
        news.clear()
        news.hideturtle()
        if x==1 and level<3:
            news.write("Extra Health", False, align="left", font=("Arial Black", 20, "normal", "bold"))
        else:
            news.write("Extra Points", False, align="left", font=("Arial Black", 20, "normal", "bold"))
    #Zastrzelenie gracza
    if math.sqrt(math.pow(gracz.xcor()-pocisk1.xcor(),2)+math.pow(gracz.ycor()-pocisk1.ycor(),2))<20:
        #winsound.PlaySound("shot.wav", winsound.SND_ASYNC)
        pocisk1.hideturtle()
        pocisk1.setposition(400,400)
        life-=1
        life_tab.clear()
        if life>0:
            life_str="Health: %s" %life
            life_tab.write(life_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
            life_tab.hideturtle()
        else:
            life_str="Health: %s" %life
            life_tab.write(life_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
            life_tab.hideturtle()
            gracz.setposition(400,400)
            k=0
    #Dotknięcie bonusu
    if math.sqrt(math.pow(gracz.xcor()-bonus.xcor(),2)+math.pow(gracz.ycor()-bonus.ycor(),2))<20:
        bonus.hideturtle()
        bonus.setposition(400,400)
        if x==1:
            life+=1*punktacja
            life_tab.clear()
            life_str="Health: %s" %life
            life_tab.write(life_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
            life_tab.hideturtle()
        else:
            wynik+=3*punktacja
            wynik_tab.clear()
            wynik_str="Points: %s" %wynik
            wynik_tab.write(wynik_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
            wynik_tab.hideturtle()
        news.clear()
        sbonus=1
    #Przemieszczanie bonusu
    if sbonus==2:
        bonus.sety(bonus.ycor()-vbonus)
    #Przemieszczanie pocisku
    if spocisk==2:
        pocisk.sety(pocisk.ycor()+vpocisk)
    #Przemieszczanie pocisku przeciwnika
    if spocisk1==2:
        pocisk1.sety(pocisk1.ycor()-vpocisk1)
    #Przerwanie niecelnego strzału
    if pocisk.ycor()>300:
        pocisk.hideturtle()
        pocisk.setposition(-400,-400)
        spocisk=1
    #Przerwanie niecelnego bonusu
    if bonus.ycor()<-400:
        bonus.hideturtle()
        bonus.setposition(-400,-400)
        sbonus=1
        news.clear()
    #Przerwanie niecelnego strzału przeciwnika
    if pocisk1.ycor()<-390:
        pocisk1.hideturtle()
        pocisk1.setposition(-400,-400)
        spocisk1=1
    #Zmiana poziomu
    if wynik>9 and c1==0:
        c1=1
        level=2
        level_tab.clear()
        level_str="Level: %s" %level
        level_tab.write(level_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        level_tab.hideturtle()
        agresja=20
        punktacja=2
        vpocisk1=35
        vpocisk=35
        vprzeciwnik=2.5
        for i in range(1):
            przeciwnicy.append(turtle.Turtle())
        for przeciwnik in przeciwnicy:
            przeciwnik.shape("enemy.gif")
            przeciwnik.speed(0)
            przeciwnik.penup()
            przeciwnik.setposition(random.randint(-250,250),random.randint(150,250))
    if wynik>29 and c2==0:
        c2=1
        level=3
        level_tab.clear()
        level_str="Level: %s" %level
        level_tab.write(level_str, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        level_tab.hideturtle()
        agresja=0
        punktacja=3
        vpocisk=40
        vpocisk1=40
        vprzeciwnik=3
        for i in range(1):
            przeciwnicy.append(turtle.Turtle())
        for przeciwnik in przeciwnicy:
            przeciwnik.shape("enemy.gif")
            przeciwnik.speed(0)
            przeciwnik.penup()
            przeciwnik.setposition(random.randint(-200,200),random.randint(150,250))
    #Koniec gry
    if k==0:
        break
end=turtle.Turtle()
end.setposition(-250,-70)
end.color("red")
wynik_str=" Game over \nwith %s points" %wynik
end.write(wynik_str, False, align="Left", font=("Arial", 70, "normal"))
end.hideturtle()
#Pętla główna
turtle.mainloop()

