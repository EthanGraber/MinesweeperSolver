#import sweeper #TODO make sweeper importable
import pygame
from pygame.locals import *
pygame.init()

class Box(pygame.sprite.Sprite):
	def __init__(self):
		super(Box, self).__init__() #allows Box to inherit from pygame Sprite
		self.image = pygame.image.load('box.png').convert()
		self.image.set_colorkey((255,255,255), RLEACCEL) #removes white background from sprite
	def setrect(self, x, y):
		self.rect = (x, y)

all_sprites = pygame.sprite.Group()

#Determines size of board
l = int(input("length: "))
h = int(input("heigh: "))

#Creates screen based on size and makes it white
screen = pygame.display.set_mode((l*75,h*75))
screen.fill((255,255,255))


y_pos = 0
for i in range(h):
	x_pos = 0
	for i in range(l):
		box = Box()
		box.setrect(x_pos, y_pos)
		all_sprites.add(box)
		x_pos += 75
	y_pos += 75

for entity in all_sprites:
	screen.blit(entity.image, entity.rect)
pygame.display.flip()

on = True
while on:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				on = False
		elif event.type == QUIT:
			on = False
