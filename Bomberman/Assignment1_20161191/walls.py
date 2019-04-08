class Walls:
	def __init__(self,rows,columns):
		self.rows=rows
		self.columns=columns
		
	def a_rough_board(self):
		x=self.rows
		y=self.columns
		Game=[[' ' for l in range(y)]for m in range(x)]
		for i in range(x):
			for j in range(y):
				if i == 0 or i==1 or i==x-1 or i==x-2:
					Game[i][j]='#'
				elif j<4:
					Game[i][j]='#'
				elif j>=y-4 and j<y:
					Game[i][j]='#'
				elif i%4==0 and j%8==0:
					Game[i][j]='#'
					Game[i][j+1]='#'
					Game[i][j+2]='#'
					Game[i][j+3]='#'
					Game[i+1][j]='#'
					Game[i+1][j+1]='#'
					Game[i+1][j+2]='#'
					Game[i+1][j+3]='#'
				##else:
				##	Game[i][j]=' '
		return Game

