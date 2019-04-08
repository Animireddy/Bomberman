from board import *
from bricks import *
from bomberman import *
from enemy import *
from bomb import *
import time
import getch
import os
import signal
TIMEOUT = 1
b=Board(1)
b1=b.place_man()
for i in b1:
	for j in i:
		print(j,end='')
	print(' ')

k=b.enemy_cnt()
l11=k
shuf=['a','d','w','s']
def interrupted(signum,frame):
	print ('interrupted')
signal.signal(signal.SIGALRM,interrupted)

def input():
	try:
		c=getch.getch()
		return c
	except:
		return
vara=0
vari=0
k3=b1
k1=[]
varj=0
bl=[]
x1=2
y1=4
a123=0
while(1):
	signal.alarm(TIMEOUT)
	os.system('clear')

	x_cor_e=b.ret_x_cor_e()
	y_cor_e=b.ret_y_cor_e()

	for i in range(k):
		random.shuffle(shuf)
		x_e=x_cor_e[i]
		y_e=y_cor_e[i]		
		k2=b.movement(shuf[0],x_e,y_e,i,2)
	for l1 in k2:
		for m1 in l1:
			print(m1,end='')
		print(' ')
	print("Game Score:", b.game_score())
	c=input()
	x_cor_b=b.ret_x_cor_b()
	y_cor_b=b.ret_y_cor_b()
	x_b=b.ret_x_cor_bomb()
	y_b=b.ret_y_cor_bomb()

	for i in range(k):
		if x_cor_e[i] == x_cor_b and y_cor_e[i] == y_cor_b:
			a123=1
	if a123 == 1:
	 	print("Game over, You were killed")
	 	break 
	if b.game_end() == 0:
	 	print("You won the game")
	 	break

	if c=='q':
		print("You quit the game")
		break

	if time.time()>=vari and vari!=0:
		varj=1
		print(k3[x1][y1])
		if k3[x1][y1]=='[' or k3[x1][y1-4]=='[' or k3[x1][y1+4]=='[' or k3[x1-2][y1]=='[' or k3[x1+2][y1]=='[':
			bl=b.blast(x1,y1,k3)
			for l in bl:
				for m in l:
					print(m,end='')
				print(' ')
			print("Game Score:", b.game_score())
			print("Game Over")
			break
		else:
			bl=b.blast(x1,y1,k3)
			x2=x1
			y2=y1
			for l in bl:
				for m in l:
					print(m,end='')
				print(' ')
			print("Game Score:", b.game_score())
	if time.time() >= vari+1 and varj==1:
		bm=b.after_blast (x1,y1,bl)
		x1=-1
		y1=-1
		for l in bm:
			for m in l:
				print(m,end='')
			print(' ')
		print("Game Score:", b.game_score())
	if c=='a' or c=='d' or c=='w' or c=='s':
		if vara==1:
			k1=b.movement(c,x_cor_b,y_cor_b,-1,1)
			k3=b.bomb(x_b,y_b,k1)
			x1=x_b
			y1=y_b
			for l in k3:
				for m in l:
					print(m,end='')
				print(' ')
			print("Game Score:", b.game_score())

			vara = 0
		else:
			k1=b.movement(c,x_cor_b,y_cor_b,-1,1)
			for l in k1:
				for m in l:
					print(m,end='')
				print(' ')
			print("Game Score:", b.game_score())


	elif c=='b':
		vara=1
		vari=time.time()+3
		for l in k1:
			for m in l:
				print(m,end='')
			print(' ')
		print("Game Score:", b.game_score())

	elif c=="None":
		print("Invalid Character")
	signal.alarm(0)