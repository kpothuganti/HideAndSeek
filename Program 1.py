from cs1graphics import *
from time import sleep

#frame1 setup

HideAndSeek = Canvas(1000,800)
HideAndSeek.setBackgroundColor('lightblue')
HideAndSeek.setTitle('HideAndSeek')

grass = Rectangle(1000,300,Point(500,750))
grass.setFillColor('lightgreen')
grass.setBorderColor('lightgreen')
HideAndSeek.add(grass)

#sun

sun = Layer()

main = Circle(150)
main.setFillColor('yellow')
main.setBorderColor('orange')
main.setBorderWidth(2)
sun.add(main)
ray1 = Circle(175)
ray1.setFillColor('transparent')
ray1.setBorderColor('orange')
ray1.setBorderWidth(4)
sun.add(ray1)
ray2 = Circle(161)
ray2.setFillColor('transparent')
ray2.setBorderColor('orange')
ray2.setBorderWidth(3)
sun.add(ray2)

p1 = Path(Point(5,187), Point(5,245))
p1.setBorderWidth(5)
p1.setBorderColor('orange')
sun.add(p1)

p2 = Path(Point(67, 174), Point(90,230))
p2.setBorderWidth(5)
p2.setBorderColor('orange')
sun.add(p2)

p3 = Path(Point(130, 135), Point(163,183))
p3.setBorderWidth(5)
p3.setBorderColor('orange')
sun.add(p3)

p4 = Path(Point(165, 90), Point(213,122))
p4.setBorderWidth(5)
p4.setBorderColor('orange')
sun.add(p4)

p5 = Path(Point(182, 45), Point(240,60))
p5.setBorderWidth(5)
p5.setBorderColor('orange')
sun.add(p5)

p6 = Path(Point(187,5), Point(245,5))
p6.setBorderWidth(5)
p6.setBorderColor('orange')
sun.add(p6)

HideAndSeek.add(sun)

#cloud1

cloud1 = Layer()
c1 = Circle(50, Point(0,35))
c1.setFillColor('white')
c1.setBorderWidth(0)
cloud1.add(c1)

c2 = Circle(50, Point(75,35))
c2.setFillColor('white')
c2.setBorderWidth(0)
cloud1.add(c2)

c3 = Circle(50, Point(150,35))
c3.setFillColor('white')
c3.setBorderWidth(0)
cloud1.add(c3)

c4 = Circle(50,Point(38,0))
c4.setFillColor('white')
c4.setBorderWidth(0)
cloud1.add(c4)

c5 = Circle(50,Point(113,0))
c5.setFillColor('white')
cloud1.add(c5)
c5.setBorderWidth(0)

cloud1.moveTo(370,50)
HideAndSeek.add(cloud1)

#cloud2

cloud2 = Layer()
c6 = Circle(50, Point(0,35))
c6.setFillColor('white')
c6.setBorderWidth(0)
cloud2.add(c6)

c7 = Circle(50, Point(75,35))
c7.setFillColor('white')
c7.setBorderWidth(0)
cloud2.add(c7)

c8 = Circle(50, Point(150,35))
c8.setFillColor('white')
c8.setBorderWidth(0)
cloud2.add(c8)

c9 = Circle(50,Point(38,0))
c9.setFillColor('white')
c9.setBorderWidth(0)
cloud2.add(c9)

c10 = Circle(50,Point(113,0))
c10.setFillColor('white')
c10.setBorderWidth(0)
cloud2.add(c10)

cloud2.moveTo(750,50)
HideAndSeek.add(cloud2)

#frame1 tree

trunk = Rectangle(50,250, Point(170,600))
trunk.setFillColor('brown')
trunk.setBorderWidth(0)
branch1 = Polygon(Point(180,590), Point(180,550), Point(280, 480))
branch1.setFillColor('brown')
branch1.setBorderWidth(0)
branch2 = Polygon(Point(160,620), Point(160,580), Point(70,510))
branch2.setFillColor('brown')
branch2.setBorderWidth(0)
leaves = Ellipse(300,225, Point(170,400))
leaves.setFillColor('darkgreen')
leaves.setBorderWidth(0)
leaves1 = Circle(100, Point(170,425))
leaves1.setFillColor('darkgreen')
leaves1.setBorderWidth(0)
HideAndSeek.add(trunk)
HideAndSeek.add(branch2)
HideAndSeek.add(branch1)
HideAndSeek.add(leaves)
HideAndSeek.add(leaves1)

#older penguin build

penguin = Layer()
body = Circle(60)
body.setFillColor('blue')
body.setBorderWidth(0)
penguin.add(body)
fur = Ellipse(90,120)
fur.setFillColor('white')
fur.setBorderWidth(0)
penguin.add(fur)
head = Circle(30, Point(0,-65))
head.setFillColor('blue')
head.setBorderWidth(0)
penguin.add(head)
cornea1 = Circle(12, Point(-11,-73))
cornea1.setFillColor('white')
cornea1.setBorderWidth(0)
cornea2 = Circle(12, Point(11,-73))
cornea2.setFillColor('white')
cornea2.setBorderWidth(0)
penguin.add(cornea2)
penguin.add(cornea1)
pupil1 = Circle(6, Point(-11,-73))
pupil1.setFillColor('black')
pupil1.setBorderWidth(0)
penguin.add(pupil1)
pupil2 = Circle(6, Point(11, -73))
pupil2.setFillColor('black')
pupil2.setBorderWidth(0)
penguin.add(pupil2)
beak = Polygon(Point(-20,-55), Point(20,-55), Point(0,-35))
beak.setFillColor('orange')
beak.setBorderWidth(0)
penguin.add(beak)
foot1 = Polygon(Point(-20,50), Point(-20,70), Point(-55,70))
foot1.setFillColor('orange')
foot1.setBorderWidth(0)
penguin.add(foot1)
foot2 = Polygon(Point(20,50), Point(20,70), Point(55,70))
foot2.setFillColor('orange')
foot2.setBorderWidth(0)
penguin.add(foot2)
penguin.moveTo(400,600)
HideAndSeek.add(penguin)

#older penguin speech

text1 = Text("I'm playing hide and seek with my little brother!")
text1.moveTo(440,490)
text1.setFontColor('black')
HideAndSeek.add(text1)
sleep(3)
HideAndSeek.remove(text1)

#older penguin move off frame

timeDelay = 0.25
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
HideAndSeek.remove(penguin)

#frame2 setup

HideAndSeek.setAutoRefresh(False)

HideAndSeek.remove(trunk)
HideAndSeek.remove(branch2)
HideAndSeek.remove(branch1)
HideAndSeek.remove(leaves)
HideAndSeek.remove(leaves1)

#pine trees

pine = Layer()
trunk = Rectangle(50,250)
trunk.setFillColor('brown')
trunk.setBorderWidth(0)
pine.add(trunk)
l1 = Polygon(Point(-125,-50), Point(125,-50),Point(0,-125))
l1.setFillColor('darkgreen')
l1.setBorderWidth(0)
pine.add(l1)
l2 = Polygon(Point(-100,-100), Point(100,-100), Point(0,-175))
l2.setFillColor('darkgreen')
l2.setBorderWidth(0)
pine.add(l2)             
pine.moveTo(125,600)
minipine1 = pine.clone()
minipine1.scale(0.5)
minipine1.moveTo(295,550)
minipine2 = pine.clone()
minipine2.scale(0.75)
minipine2.moveTo(900,560)
minipine3 = pine.clone()
minipine3.scale(0.85)
minipine3.moveTo(695,585)
HideAndSeek.add(minipine3)
HideAndSeek.add(minipine2)
HideAndSeek.add(minipine1)
HideAndSeek.add(pine)

#pond

pond = Ellipse(250,125, Point(350,700))
pond.setFillColor('blue')
pond.setBorderWidth(0)
HideAndSeek.add(pond)

#younger penguin build

bro = penguin.clone()
bro.scale(0.65)
bro.moveTo(1450,700)
HideAndSeek.add(bro)
HideAndSeek.setAutoRefresh(True)

#younger penguin move on frame

bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)
bro.move(-75,0)
sleep(timeDelay)

#younger penguin speech

text2 = Text("I'm hiding from my big brother. \n             Wish me luck!")
text2.setFontColor('black')
text2.moveTo(670,615)
HideAndSeek.add(text2)
sleep(4)
HideAndSeek.remove(text2)

#younger penguin move off screen

bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
HideAndSeek.remove(bro)

#frame3 setup

HideAndSeek.setAutoRefresh(False)

HideAndSeek.remove(pine)
HideAndSeek.remove(minipine1)
HideAndSeek.remove(minipine2)
HideAndSeek.remove(minipine3)
HideAndSeek.remove(pond)

#younger penguin (hidden) appearance

bro.moveTo(150,625)
HideAndSeek.add(bro)

#bush

bush = Layer()
a1 = Ellipse(200,150)
a1.setFillColor('darkgreen')
a1.setBorderWidth(0)
bush.add(a1)
a2 = Ellipse(150,200)
a2.setFillColor('darkgreen')
a2.setBorderWidth(0)
a2.moveTo(0,-15)
bush.add(a2)
bush.moveTo(150,600)
HideAndSeek.add(bush)

#older penguin walk on 2

penguin.moveTo(1450,600)
HideAndSeek.add(penguin)
HideAndSeek.setAutoRefresh(True)
penguin.move(-75,0)
sleep(timeDelay)
penguin.move(-75,0)
sleep(timeDelay)
penguin.move(-75,0)
sleep(timeDelay)
penguin.move(-75,0)
sleep(timeDelay)
penguin.move(-75,0)
sleep(timeDelay)
penguin.move(-75,0)
sleep(timeDelay)
penguin.move(-75,0)
sleep(timeDelay)
penguin.move(-75,0)
sleep(timeDelay)

#older penguin speech

text3 = Text("I still haven't found my brother. \n  I wonder where he could be...")
text3.setFontColor('black')
text3.moveTo(800,480)
HideAndSeek.add(text3)
sleep(3)
HideAndSeek.remove(text3)

#younger penguin sneak speech

text4 = Text("Pssst...")
text4.setFontColor('black')
text4.moveTo(235,500)
HideAndSeek.add(text4)
sleep(1.5)
HideAndSeek.remove(text4)

#older penguin confused speech

text5 = Text("HUH \nWho said that??")
text5.setFontColor('black')
text5.moveTo(800,480)
HideAndSeek.add(text5)
sleep(1.5)
HideAndSeek.remove(text5)

#younger penguin moves out from behind bush

bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)

#brothers conversing

text6 = Text("There you are!! \nI looked everywhere for you!")
text6.setFontColor('black')
text6.moveTo(800,480)
HideAndSeek.add(text6)
sleep(2)
HideAndSeek.remove(text6)
text7 = Text("I win!!")
text7.setFontColor('black')
text7.moveTo(630,550)
HideAndSeek.add(text7)
sleep(1.5)
HideAndSeek.remove(text7)
text8 = Text("Yeah, yeah you won. \nNow let's go home before we get in trouble!")
text8.setFontColor('black')
text8.moveTo(800,480)
HideAndSeek.add(text8)
sleep(2.5)
HideAndSeek.remove(text8)

#brothers walk off frame

penguin.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
penguin.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)
bro.move(75,0)
sleep(timeDelay)

#the end

text9 = Text('The \nEnd')
text9.setFontColor('white')
text9.setFontSize(50)
text9.moveTo(500,300)
HideAndSeek.add(text9)
