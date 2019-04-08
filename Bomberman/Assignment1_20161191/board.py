from bricks import Bricks
from bomberman import Bomberman
from enemy import Enemy
from bomb import Bomb
import random
class Board:
	def __init__(self,vari):
		self.vari=vari
		self.c1=Bricks(42,84,50)
		self.Board=self.c1.board_after_bricks()
		self.cnt=self.c1.return_count()
		self.enemy_array=self.c1.enemy_array()
		self.enemy_array1=self.c1.enemy_array1()
		self.x_v=2
		self.y_v=4
		self.x_b=2
		self.y_b=4
		#self.game_over=0
		self.score=0
		self.score1=0
		self.l11=self.cnt
	def place_man(self):
		b2=Bomberman(2,4)
		b2=b2.create_man(self.Board)
		return b2		

	def movement(self,direction,x_cor,y_cor,index,type_c):
		if direction == 'a':
			if self.Board[x_cor][y_cor-4] =='#' or self.Board[x_cor][y_cor-4]=='%':
				return self.Board
			else:
				self.Board[x_cor][y_cor]=' '
				self.Board[x_cor][y_cor+1]=' '
				self.Board[x_cor][y_cor+2]=' '
				self.Board[x_cor][y_cor+3]=' '
				self.Board[x_cor+1][y_cor]=' '
				self.Board[x_cor+1][y_cor+1]=' '
				self.Board[x_cor+1][y_cor+2]=' '
				self.Board[x_cor+1][y_cor+3]=' '
				y_cor=y_cor-4
				if type_c == 1:
					b2=Bomberman(x_cor,y_cor)
					b21=b2.create_man(self.Board)
					self.x_v=x_cor
					self.y_v=y_cor
					self.x_b=x_cor
					self.y_b=y_cor
					return b21
				elif type_c == 2:
					b3=Enemy(x_cor,y_cor)
					b3=b3.create_enemy(self.Board)
					self.enemy_array[index]=x_cor
					self.enemy_array1[index]=y_cor
					return b3

		elif direction == 'd':
			if self.Board[x_cor][y_cor+4] =='#' or self.Board[x_cor][y_cor+4]=='%':
				return self.Board
			else:
				self.Board[x_cor][y_cor]=' '
				self.Board[x_cor][y_cor+1]=' '
				self.Board[x_cor][y_cor+2]=' '
				self.Board[x_cor][y_cor+3]=' '
				self.Board[x_cor+1][y_cor]=' '
				self.Board[x_cor+1][y_cor+1]=' '
				self.Board[x_cor+1][y_cor+2]=' '
				self.Board[x_cor+1][y_cor+3]=' '
				y_cor=y_cor+4
				if type_c == 1:
					b2=Bomberman(x_cor,y_cor)
					b21=b2.create_man(self.Board)
					self.x_v=x_cor
					self.y_v=y_cor
					self.x_b=x_cor
					self.y_b=y_cor
					return b21
				elif type_c == 2:
					b3=Enemy(x_cor,y_cor)
					b3=b3.create_enemy(self.Board)
					self.enemy_array[index]=x_cor
					self.enemy_array1[index]=y_cor
					return b3

		elif direction == 's':
			if self.Board[x_cor+2][y_cor] =='#' or self.Board[x_cor+2][y_cor]=='%':
				return self.Board
			else:
				self.Board[x_cor][y_cor]=' '
				self.Board[x_cor][y_cor+1]=' '
				self.Board[x_cor][y_cor+2]=' '
				self.Board[x_cor][y_cor+3]=' '
				self.Board[x_cor+1][y_cor]=' '
				self.Board[x_cor+1][y_cor+1]=' '
				self.Board[x_cor+1][y_cor+2]=' '
				self.Board[x_cor+1][y_cor+3]=' '
				x_cor=x_cor+2
				if type_c == 1:
					b2=Bomberman(x_cor,y_cor)
					b21=b2.create_man(self.Board)
					self.x_v=x_cor
					self.y_v=y_cor
					self.x_b=x_cor
					self.y_b=y_cor
					return b21
				elif type_c == 2:
					b3=Enemy(x_cor,y_cor)
					b3=b3.create_enemy(self.Board)
					self.enemy_array[index]=x_cor
					self.enemy_array1[index]=y_cor
					return b3

		elif direction == 'w':
			if self.Board[x_cor-2][y_cor] =='#' or self.Board[x_cor-2][y_cor]=='%':
				return self.Board
			else:
				self.Board[x_cor][y_cor]=' '
				self.Board[x_cor][y_cor+1]=' '
				self.Board[x_cor][y_cor+2]=' '
				self.Board[x_cor][y_cor+3]=' '
				self.Board[x_cor+1][y_cor]=' '
				self.Board[x_cor+1][y_cor+1]=' '
				self.Board[x_cor+1][y_cor+2]=' '
				self.Board[x_cor+1][y_cor+3]=' '
				x_cor=x_cor-2
				if type_c == 1:
					b2=Bomberman(x_cor,y_cor)
					b21=b2.create_man(self.Board)
				#	b2.set_x_cor(x_cor)
				#	b2.set_y_cor(y_cor)
					self.x_v=x_cor
					self.y_v=y_cor
					self.x_b=x_cor
					self.y_b=y_cor
					return b21
				elif type_c == 2:
					b3=Enemy(x_cor,y_cor)
					b3=b3.create_enemy(self.Board)
					self.enemy_array1[index]=y_cor
					self.enemy_array[index]=x_cor
					return b3
		
	def ret_x_cor_b(self):
		return self.x_v
	def ret_y_cor_b(self):
		return self.y_v
	def ret_x_cor_e(self):
		return self.enemy_array
	def ret_y_cor_e(self):
		return self.enemy_array1
	def enemy_cnt(self):
		return self.cnt
	def enemy_arr(self):
		return self.enemy_array
	def enemy_arr1(self):
		return self.enemy_array1
	def ret_x_cor_bomb(self):
		return self.x_b
	def ret_y_cor_bomb(self):
		return self.y_b
	def game_score(self):
		return self.score

	def bomb(self,x,y,array):
		array[x][y]='B'
		array[x][y+1]='B'
		array[x][y+2]='B'
		array[x][y+3]='B'
		array[x+1][y]='B'
		array[x+1][y+1]='B'
		array[x+1][y+2]='B'
		array[x+1][y+3]='B'
		return array
	def blast(self,x,y,array):
		k=self.cnt
		if array[x][y]=='(':
			for i in range(k):
				if self.enemy_array[i]==x and self.enemy_array1[i]==y:
					self.enemy_array[i]=-1
					self.enemy_array1[i]=-1
					self.score=self.score+100
					self.l11=self.l11-1
		array[x][y]='^'
		array[x][y+1]='^'
		array[x][y+3]='^'
		array[x][y+2]='^'
		array[x+1][y]='^'
		array[x+1][y+1]='^'
		array[x+1][y+3]='^'
		array[x+1][y+2]='^'

		if array[x][y-4]!='#':
			if array[x][y-4]=='(':
				for i in range(k):
					if self.enemy_array[i]==x and self.enemy_array1[i]==y-4:
						self.enemy_array[i]=-1
						self.enemy_array1[i]=-1
						self.score=self.score+100
						self.l11=self.l11-1

			if array[x][y-4]=='%':
				self.score=self.score+20
			array[x][y-4]='^'
			array[x][y-3]='^'
			array[x][y-2]='^'
			array[x][y-1]='^'
			array[x+1][y-1]='^'
			array[x+1][y-2]='^'
			array[x+1][y-3]='^'
			array[x+1][y-4]='^'
		if array[x][y+4]!='#':
			if array[x][y+4]=='(':
				for i in range(k):
					if self.enemy_array[i]==x and self.enemy_array1[i]==y+4:
						self.enemy_array[i]=-1
						self.enemy_array1[i]=-1
						self.score=self.score+100
						self.l11=self.l11-1
			elif array[x][y+4]=='%':
				self.score=self.score+20

			array[x][y+4]='^'
			array[x][y+5]='^'
			array[x][y+6]='^'
			array[x][y+7]='^'
			array[x+1][y+4]='^'
			array[x+1][y+5]='^'
			array[x+1][y+6]='^'
			array[x+1][y+7]='^'
		if array[x-2][y]!='#':
			if array[x-2][y]=='(':
				for i in range(k):
					if self.enemy_array[i]==x-2 and self.enemy_array1[i]==y:
						self.enemy_array[i]=-1
						self.enemy_array1[i]=-1
						self.score=self.score+100
						self.l11=self.l11-1
			elif array[x-2][y]=='%':
				self.score=self.score+20

			array[x-2][y]='^'
			array[x-2][y+1]='^'
			array[x-2][y+2]='^'
			array[x-2][y+3]='^'
			array[x-1][y]='^'
			array[x-1][y+1]='^'
			array[x-1][y+2]='^'
			array[x-1][y+3]='^'
		if array[x+2][y]!='#':
			if array[x+2][y]=='(':
				for i in range(k):
					if self.enemy_array[i]==x+2 and self.enemy_array1[i]==y:
						self.enemy_array[i]=-1
						self.enemy_array1[i]=-1
						self.score=self.score+100
						self.l11=self.l11-1
			elif array[x+2][y]=='%':
				self.score=self.score+20

			array[x+2][y]='^'
			array[x+2][y+1]='^'
			array[x+2][y+2]='^'
			array[x+2][y+3]='^'
			array[x+3][y]='^'
			array[x+3][y+1]='^'
			array[x+3][y+2]='^'
			array[x+3][y+3]='^'
		return array

	def after_blast(self,x,y,array):
		array[x][y]=' '
		array[x][y+1]=' '
		array[x][y+3]=' '
		array[x][y+2]=' '
		array[x+1][y]=' '
		array[x+1][y+1]=' '
		array[x+1][y+3]=' '
		array[x+1][y+2]=' '

		if array[x][y-4]=='^':
			array[x][y-4]=' '
			array[x][y-3]=' '
			array[x][y-2]=' '
			array[x][y-1]=' '
			array[x+1][y-1]=' '
			array[x+1][y-2]=' '
			array[x+1][y-3]=' '
			array[x+1][y-4]=' '

		if array[x][y+4]=='^':
			array[x][y+4]=' '
			array[x][y+5]=' '
			array[x][y+6]=' '
			array[x][y+7]=' '
			array[x+1][y+4]=' '
			array[x+1][y+5]=' '
			array[x+1][y+6]=' '
			array[x+1][y+7]=' '
		if array[x-2][y]=='^':
			array[x-2][y]=' '
			array[x-2][y+1]=' '
			array[x-2][y+2]=' '
			array[x-2][y+3]=' '
			array[x-1][y]=' '
			array[x-1][y+1]=' '
			array[x-1][y+2]=' '
			array[x-1][y+3]=' '
		if array[x+2][y]=='^':
			array[x+2][y]=' '
			array[x+2][y+1]=' '
			array[x+2][y+2]=' '
			array[x+2][y+3]=' '
			array[x+3][y]=' '
			array[x+3][y+1]=' '
			array[x+3][y+2]=' '
			array[x+3][y+3]=' '
		return array

	def game_end(self):
		return self.l11




			
			



			
		

