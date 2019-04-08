from bricks import *
class Bomb:
	def __init__(self,x_cor,y_cor):
		self.x_cor=x_cor
		self.y_cor=y_cor
	def create_bomb(self,Bomb):
		x=self.x_cor
		y=self.y_cor
		Bomb[x][y]='B'
		Bomb[x][y+1]='B'
		Bomb[x][y+2]='B'
		Bomb[x][y+3]='B'
		Bomb[x+1][y]='B'
		Bomb[x+1][y+1]='B'
		Bomb[x+1][y+2]='B'
		Bomb[x+1][y+3]='B'
		return Bomb
