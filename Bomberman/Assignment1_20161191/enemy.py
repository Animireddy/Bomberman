from bricks import *
class Enemy:
	def __init__(self,x_cor,y_cor):
		self.x_cor=x_cor
		self.y_cor=y_cor
	def create_enemy(self,Enemy):
		x=self.x_cor
		y=self.y_cor
		if(x!=-1 and y!=-1):
			Enemy[x][y]='('
			Enemy[x][y+1]='<'
			Enemy[x][y+2]='>'
			Enemy[x][y+3]=')'
			Enemy[x+1][y]=' '
			Enemy[x+1][y+1]='"'
			Enemy[x+1][y+2]='"'
			Enemy[x+1][y+3]=' '
			return Enemy
		else:
			return Enemy

