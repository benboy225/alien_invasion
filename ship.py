"""This class will creat an instance of the ship and put it at its right location on the screen"""


import pygame as pg 

class Ship:
	
	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings


		#load the ship image and get its rect
		self.image = pg.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()


		#Start position in mid bottom
		self.rect.midbottom = self.screen_rect.midbottom

		#set up the speed of the ship
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right:
			self.x += self.settings.ship_speed

		if self.moving_left:
			self.x -= self.settings.ship_speed

		if self.moving_up:
			self.y -= self.settings.ship_speed

		if self.moving_down:
			self.y += self.settings.ship_speed

		#update position
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image,self.rect)



