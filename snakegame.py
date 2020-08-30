import pygame
import random
import os
import time
from gamewellcomescreen import wellcome_snake

'''def wellcome_snake():

	pygame.init()
	
	WHITE = (255,255,255)
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption("Snake Game")
	wellcome_font = pygame.font.Font("freesansbold.ttf",30)
	git_repo = pygame.font.Font('fonts\Roboto-Light.ttf',13)
	bg_image = pygame.image.load("images\wellcomepic.jpg")
	bg_image = pygame.transform.scale(bg_image, (150, 160))

	start = False
	while not start:
		
		screen.fill(WHITE)
		screen.blit(bg_image,((600/3),10))

		msg = wellcome_font.render("Wellcome to Snake Game",True,(0,0,0))
		msg_pos = msg.get_rect()
		msg_pos.center = (abs(570/2),abs(450/2))
		screen.blit(msg,msg_pos)

		repo_link = git_repo.render("Source Code at : git@github.com:samiali12/Snake-game-in-python.git",True,(0,0,0))
		repo_link_pos = repo_link.get_rect()
		repo_link_pos.center = ( (210), (750)/2)
		screen.blit(repo_link,repo_link_pos)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				start = True
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_RETURN:

					start = True


		pygame.display.update()
'''

wellcome_snake()

pygame.init()

#enable this for sound effect

#try:
#	pygame.mixer.init()

#except pygame.error:
#	print("Game Sound Disable because ")
#	print("DirectSoundCreate : No Audio Device Found")

pygame.mouse.set_visible(0)

 # Constant Color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

# height and width of window
SCREEN_HEIGHT = 500
SCREEN_WIDTH  = 500

bg_image = pygame.image.load("images\\bg.png")
bg_image = pygame.transform.scale(bg_image, (500, 500))
icon = pygame.image.load("images\\icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption("Snake Game")

pygame.display.update()

# text font include file
font = pygame.font.Font("freesansbold.ttf",15)

# Draw Well Come Screen Message

def wellcome_snake():

	time.sleep(10)

	screen.fill(WHITE)
	wellcome_font = pygame.font.Font("freesansbold.ttf",30)
	msg = wellcome_font.render("Wellcome to Snake Game",True,GREEN,WHITE)
	msg_pos = msg.get_rect()
	msg_pos.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
	screen.blit(msg,msg_pos)


#plot boudries around the snake ground

def plot_boundary(score ,high_score):

	pygame.draw.rect(screen,RED,[10,5,470,5])
	pygame.draw.rect(screen,RED,[10,5,5,50])
	score_draw(score,high_score)
	pygame.draw.rect(screen,RED,[480,5,5,50])
	pygame.draw.rect(screen,RED,[10,50,470,5])

			# Left Boundries
	pygame.draw.rect(screen,RED,[10,50,5,430])
			# bottom Boundries
	pygame.draw.rect(screen,RED,[10,480,470,5])
	pygame.draw.rect(screen,RED,[480,5,5,480])


# draw score on the screen 
def score_draw(score,high_score):

	score = font.render("Score : "+str(score),True,WHITE)
	high_score_text =font.render("High Score : "+str(high_score),True,WHITE)

	score_pos = score.get_rect()
	high_score_pos = high_score_text.get_rect()

	score_pos.center = (160/2,60/2)
	high_score_pos.center = (400/2,60/2)
	
	screen.blit(score,score_pos)
	screen.blit(high_score_text,high_score_pos)
	

def draw_snake(length_list , snake_size):

	for x , y in length_list:
		pygame.draw.rect(screen,BLACK,[x,y,snake_size,snake_size])



def game_loop():

	food_x = random.randint(20,(SCREEN_WIDTH)/2)
	food_y = random.randint(45,(SCREEN_HEIGHT)/2)

	snake_length_list =  []
	snake_length = 1


	snake_axis_position = 100
	snake_yaxis_position = 200

	GAME_STOP = False
	GAME_OVER = False

	score = 0 
	#high_score =""
	clock = pygame.time.Clock()

	snake_x_pos = 0
	snake_y_pos = 0

	snake_width = 10
	snake_height = 10

	top_border = 50
	left_border = 10
	right_border = 480
	bottom_border = 480

	# if user break high score then snake of speed in increase

	snake_speed = 3


		# check if file not exits
	if (not os.path.exists("highest_score.txt")):
		with open("highest_score.txt","w") as file:
			file.write("0")

	else:
		with open("highest_score.txt","r") as file:
			high_score = file.read()



	while not GAME_STOP:



		if GAME_OVER:

			#try:
			#	pygame.mixer.music.load("bg_music.mp3")
			#	pygame.mixer.music.play()
			#except pygame.error:
			#	pass

			screen.fill(WHITE)
			text = font.render("Game Over",True,RED,WHITE)
			text_pos = text.get_rect()
			text_pos.center = (SCREEN_WIDTH/2.1,SCREEN_HEIGHT/3)
			text2 = font.render("Press  Enter  Key  To  Continue  ...",True,RED,WHITE)
			text_pos2 = text.get_rect()
			text_pos2.center = (SCREEN_WIDTH/3,SCREEN_HEIGHT/2)

			screen.blit(text,text_pos)
			screen.blit(text2,text_pos2)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					GAME_STOP = True

				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_RETURN:
						game_loop()

		else:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:

					GAME_STOP = True
				
				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_LEFT:

						snake_x_pos -= snake_speed;
						snake_y_pos = 0

					if event.key == pygame.K_RIGHT:

						snake_x_pos += snake_speed
						snake_y_pos = 0

					if event.key == pygame.K_UP:

						snake_y_pos -= snake_speed
						snake_x_pos = 0;

					if event.key == pygame.K_DOWN:

						snake_y_pos = snake_speed
						snake_x_pos = 0
						
				
			snake_axis_position += snake_x_pos
			snake_yaxis_position += snake_y_pos

			head = []
			head.append(snake_axis_position)
			head.append(snake_yaxis_position)
			snake_length_list.append(head)
			
			if len(snake_length_list) > snake_length:
				del snake_length_list[0]

			if snake_axis_position <= 10 or snake_axis_position >= 480 or snake_yaxis_position <= 50 or snake_yaxis_position >= 480:

					GAME_OVER = True


			if head in snake_length_list[:-1]:

					GAME_OVER = True

			if  abs(snake_axis_position - food_x) < 8 and abs(snake_yaxis_position  - food_y) < 8:

				food_x = abs(random.randint(40,(SCREEN_WIDTH)/2))
				food_y = abs(random.randint(80,(SCREEN_HEIGHT)/2))
				score += 10
				snake_length +=1

				if score > int(high_score):
					high_score = str(score)
					snake_speed += 1

				with open("highest_score.txt","w") as file:
					file.write(str(high_score))


			screen.fill(WHITE)

			screen.blit(bg_image,(0,0))

			pygame.draw.rect(screen,BLUE,[food_x,food_y,10,10])

			plot_boundary(score,high_score)

			draw_snake(snake_length_list,10)
			

		pygame.display.update()
		clock.tick(30)




game_loop()

pygame.quit()