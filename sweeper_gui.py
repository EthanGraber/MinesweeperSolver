import sweeper #TODO make sweeper importable
import pygame
from pygame.locals import *
pygame.init()

class Box(pygame.sprite.Sprite):
	def __init__(self):
		super(Box, self).__init__() #allows Box to inherit from pygame Sprite
		self.image = pygame.image.load('box.png').convert() #TODO use smaller box.png?
		self.image.set_colorkey((255,255,255), RLEACCEL) #removes white background from sprite
		self.rect = self.image.get_rect()
	def moverect(self, x, y):
		self.rect.move_ip(x, y)
	def boxreveal(self, value):
		if value == '&':
			img = 'blank.png'
		elif value == 'F':
			img = 'flag.png
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
	for i in range(l):
		box = Box()
		box.moverect(x_pos, y_pos)
		all_sprites.add(box)
		x_pos += 83
	y_pos += 85


for entity in all_sprites:
	screen.blit(entity.image, entity.rect)
pygame.display.flip()

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
			print(clicked_sprites[0].rect)
