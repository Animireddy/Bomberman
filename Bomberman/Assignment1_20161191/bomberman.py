from bricks import *
class Bomberman:
	def __init__(self,x_cor,y_cor):
		self.x_cor=x_cor
		self.y_cor=y_cor
	def create_man(self,Bomber):
		x=self.x_cor
		y=self.y_cor
		Bomber[x][y]='['
		Bomber[x][y+1]='^'
		Bomber[x][y+2]='^'
		Bomber[x][y+3]=']'
		Bomber[x+1][y]=' '
		Bomber[x+1][y+1]=']'
		Bomber[x+1][y+2]='['
		Bomber[x+1][y+3]=' '
		return Bomber
		





