import pygame
import os
import random

class SnakeGame:

	def __init__(self):

		pygame.init()
	    
		pygame.mouse.set_visible(0)

		self.SCREEN_HEIGHT = 500
		self.SCREEN_WIDTH  = 500
		self.BLACK = (0,0,0)
		self.WHITE = (255,255,255)
		self.RED   = (255,0,0)
		self.GREEN = (0,255,0)
		self.BLUE  = (0,0,255)
		self.GAME_STOP = False
		self.GAME_OVER = False

		self.snake_axis_position = 100
		self.snake_yaxis_position = 200

		self.score = 0 
		self.high_score =""
		self.clock = pygame.time.Clock()

		self.snake_x_pos = 0
		self.snake_y_pos = 0

		self.snake_width = 10
		self.snake_height = 10

		self.top_border = 50
		self.left_border = 10
		self.right_border = 480
		self.bottom_border = 480

		self.snake_length_list =  []
		self.snake_length = 1

		self.food_x = random.randint(20,(self.SCREEN_WIDTH)/2)
		self.food_y = random.randint(45,(self.SCREEN_HEIGHT)/2)


		self.bg_image = pygame.image.load("bg.png")
	
		self.font = pygame.font.Font("freesansbold.ttf",20)

		self.screen = pygame.display.set_mode((self.SCREEN_HEIGHT,self.SCREEN_WIDTH))
		pygame.display.set_caption("Snake Game")

		self.loopGameWindow()


	def plot_boundary(self, score , high_score):

		pygame.draw.rect(self.screen,self.RED,[10,5,470,5])
		pygame.draw.rect(self.screen,self.RED,[10,5,5,50])
		self.score_draw(score,high_score)
		pygame.draw.rect(self.screen,self.RED,[480,5,5,50])
		pygame.draw.rect(self.screen,self.RED,[10,50,470,5])

				# Left Boundries
		pygame.draw.rect(self.screen,self.RED,[10,50,5,430])
				# bottom Boundries
		pygame.draw.rect(self.screen,self.RED,[10,480,470,5])
		pygame.draw.rect(self.screen,self.RED,[480,5,5,480])


	# draw score on the screen 
	def score_draw(self,score,high_score):

		text = self.font.render("Score : "+str(score) +"       High Score : "+high_score,True,self.WHITE)
		text_pos = text.get_rect()
		text_pos.center = (350/2,60/2)
		self.screen.blit(text,text_pos)


	def draw_snake(self,length_list , snake_size):

		for x , y in length_list:
			pygame.draw.rect(self.screen,self.BLACK,[x,y,snake_size,snake_size])

	def loopGameWindow(self):

		while not self.GAME_STOP:

			if self.GAME_OVER:


				screen.fill(WHITE)
				text = self.font.render("Game Over",True,RED,WHITE)
				text_pos = text.get_rect()
				text_pos.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
				screen.blit(text,text_pos)
				text = self.font.render("Press ( Enter Key ) to Continue",True,RED,WHITE)
				text_pos = text.get_rect()
				text_pos.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT+100/2)
				screen.blit(text,text_pos)

			else:
				
				for event in pygame.event.get():

					if event.type == pygame.QUIT:
						GAME_STOP = True

					self.screen.fill(self.WHITE)

					for event in pygame.event.get():


						if event.type == pygame.QUIT:

							self.GAME_STOP = True

						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_LEFT:

								self.snake_x_pos -= 7;
								self.snake_y_pos = 0

							if event.key == pygame.K_RIGHT:

								self.snake_x_pos += 7
								self.snake_y_pos = 0

							if event.key == pygame.K_UP:

								self.snake_y_pos -= 7
								self.snake_x_pos = 0;

							if event.key == pygame.K_DOWN:

								self.snake_y_pos = 7
								self.snake_x_pos = 0
								
					
				self.snake_axis_position += self.snake_x_pos
				self.snake_yaxis_position += self.snake_y_pos

				head = []
				head.append(self.snake_axis_position)
				head.append(self.snake_yaxis_position)
				self.snake_length_list.append(head)
				
				if len(self.snake_length_list) > self.snake_length:
					del self.snake_length_list[0]

				if self.snake_axis_position <= 10 or self.snake_axis_position >= 480 or self.snake_yaxis_position <= 50 or self.snake_yaxis_position >= 480:

					self.GAME_OVER = True

				if head in self.snake_length_list[:-1]:
					self.GAME_OVER = True

				if  abs(self.snake_axis_position - self.food_x) < 6 and abs(self.snake_yaxis_position  - self.food_y) < 6:

					self.food_x = random.randint(40,(self.SCREEN_WIDTH)/2)
					self.food_y = random.randint(60,(self.SCREEN_HEIGHT)/2)
					self.score += 10
					self.snake_length +=5

					if score > int(high_score):
						high_score = str(score)

					with open("highest_score.txt","w") as file:
						file.write(str(high_score))



				self.screen.fill(self.WHITE)

				self.bg_image = pygame.transform.scale(self.bg_image, (500, 500))
				self.screen.blit(self.bg_image,(0,0))

				pygame.draw.rect(self.screen,self.BLUE,[self.food_x,self.food_y,10,10])

				self.plot_boundary(self.score,self.high_score)

				self.draw_snake(self.snake_length_list,10)


			pygame.display.update()

			self.clock.tick(30)

s1 = SnakeGame()