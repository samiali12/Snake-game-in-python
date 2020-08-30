import pygame

def wellcome_snake():

	pygame.init()
	
	WHITE = (255,255,255)
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption("Snake Game")
	icon = pygame.image.load("images\icon.png")
	pygame.display.set_icon(icon)
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

if __name__ == '__main__':
	pass