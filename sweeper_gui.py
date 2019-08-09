#import sweeper #TODO make sweeper importable
import pygame
from pygame.locals import *
pygame.init()

class Bombbox(pygame.sprite.Sprite):
	def __init__(self):
		super(Bombbox, self).__init__()
		self.image = pygame.image.load('box.png').convert()
		self.image.set_colorkey((255,255,255), RLEACCEL)
		self.rect = self.image.get_rect()

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

l = int(input("length: "))
h = int(input("heigh: "))

y_pos = 0
for i in range(h):
	x_pos = 0
	for i in range(l):
		

box = Bombbox()
screen.blit(box.image, (0, 0))
screen.blit(box.image, (75, 0))
pygame.display.flip()

on = True
while on:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				on = False
		elif event.type == QUIT:
			on = False
