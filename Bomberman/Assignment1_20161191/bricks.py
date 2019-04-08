from walls import Walls
import random
class Bricks(Walls):
	def __init__(self,rows,columns,max_bricks):
		Walls.__init__(self,rows,columns)
		self.max_bricks=max_bricks
		self.count1=0
		self.Enemy=[]
		self.Enemy1=[]

	def board_after_bricks(self):
		count=0
		ret=Walls(self.rows,self.columns)
		Game=ret.a_rough_board()
		for i in range(2,self.rows-2):
			for j in range(4,self.columns-4):
				if (((i%4==2 and j%4==0 and random.random()<0.1) or (i%4==0 and j%8==4 and random.random()<0.1)) and (count<self.max_bricks) and (not (i== 2 and j==4)) and (not (i==4 and j==4)) and (not (i==2 and j==8))):
					Game[i][j]='%'
					Game[i][j+1]='%'
					Game[i][j+2]='%'
					Game[i][j+3]='%'
					Game[i+1][j]='%'
					Game[i+1][j+1]='%'
					Game[i+1][j+2]='%'
					Game[i+1][j+3]='%'
					count=count+1
				elif (((i%4==2 and j%4==0 and random.random()<0.1) or (i%4==0 and j%8==4 and random.random()<0.1)) and (self.count1<7) and (not (i== 2 and j==4)) and (not (i==4 and j==4)) and (not (i==2 and j==8))):
					Game[i][j]='('
					Game[i][j+1]='<'
					Game[i][j+2]='>'
					Game[i][j+3]=')'
					Game[i+1][j]=' '
					Game[i+1][j+1]='"'
					Game[i+1][j+2]='"'
					Game[i+1][j+3]=' '
					self.count1=self.count1+1
					self.Enemy.append(i)
					self.Enemy1.append(j)

		return Game	
	def return_count(self):
		return self.count1

	def enemy_array(self):
		return self.Enemy
		
	def enemy_array1(self):
		return self.Enemy1







	