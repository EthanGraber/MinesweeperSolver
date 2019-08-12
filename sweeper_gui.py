import sweeper #TODO make sweeper importable
import pygame
from pygame.locals import *
pygame.init()

class Box(pygame.sprite.Sprite):
	def __init__(self, row, col):
		super(Box, self).__init__() #allows Box to inherit from pygame Sprite
		self.image = pygame.image.load('box.png').convert() 
		self.image.set_colorkey((255,255,255), RLEACCEL) #removes white background from sprite
		self.rect = self.image.get_rect()
		self.row = row
		self.col = col
	def moverect(self, x, y):
		self.rect.move_ip(x, y)
	def boxreveal(self, value):
		if value == '#':
			img = 'box.png'
		elif value == '&':
			img = 'blank.png'
		elif value == 'F':
			img = 'flag.png'
		elif value == 'B':
			img = 'bomb.png'
		elif value == '1':
			img = '1.png'
		elif value == '2':
			img = '2.png'
		elif value == '3':
			img = '3.png'
		elif value == '4':
			img = '4.png'
		elif value == '5':
			img = '5.png'
		elif value == '6':
			img = '6.png'
		self.image = pygame.image.load(img)
		#Is it even possible to have a value higher than 6?
		
all_sprites = pygame.sprite.Group()

#Gets length and height from sweeper
l = sweeper.length
h = sweeper.height

sweeper.prettyprint(sweeper.solved_board)

#Creates screen based on size and makes it white
screen = pygame.display.set_mode((l*83,h*85))
screen.fill((255,255,255))


y_pos = 0
for i in range(h):
	x_pos = 0
	for j in range(l):
		box = Box(i, j)
		box.moverect(x_pos, y_pos)
		all_sprites.add(box)
		x_pos += 83
	y_pos += 85

def render():
	for entity in all_sprites:
		screen.blit(entity.image, entity.rect)
	pygame.display.flip()

render()

on = True
move_counter = 0
while on:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				on = False
		elif event.type == QUIT:
			on = False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]

			#rect[1] is the y coordinate of the image. Divided by 83 bc 83 pixels.
			
			col = int(clicked_sprites[0].rect[0]/83)
			row = int(clicked_sprites[0].rect[1]/85)
			
			sweeper.reveal(row, col)
			for entity in all_sprites:
				entity.boxreveal(sweeper.board[entity.row][entity.col])
			render()
