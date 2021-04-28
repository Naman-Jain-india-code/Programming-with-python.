from turtle import*
speed(10)
color('red')
for i in range(3):
		forward(300)
		left(120)

def tri(size):
	for i in range(3):
		forward(size)
		right(120)
def ser(size):
        left(60);forward(size);right(60);tri(size);left(60);forward(size*2)
        right(60);tri(size);left(60);forward(size);right(120);forward(size+(2*size))
        left(240);forward(size);left(120);forward(size);left(120);forward(size);right(120)
        forward(size)

def serpinski():
        left(60)
        forward(150)
        right(60)
        tri(150)
        goto(0,0)
        ser(75);goto(0,0);left(60);ser(37.5);left(60);ser(37.5)
        goto(0,0);left(60);left(60);forward(150);right(60);ser(37.5)
        left(240);forward(150);left(60);forward(150);right(240)

serpinski();left(180);color('blue');serpinski();right(90)
color('green');serpinski();left(180);color('orange');serpinski()
left(90);ht()







