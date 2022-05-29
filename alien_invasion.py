""" We will now create an empty game window using pygame. the objective here is to then add 
the other parts of the game later."""

import sys

import pygame as pg

from settings import Settings as st
from ship import Ship as sp
from bullet import Bullet as bl

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initialize the game, and create game resources."""
		pg.init()
		self.settings = st()

		self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pg.display.set_caption("Alien Invasion") #this is called surface

		self.ship = sp(self)
		self.bullets = pg.sprite.Group()

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			# Watch for keyboard and mouse events
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
			
	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pg.event.get():
				if event.type == pg.QUIT:
					sys.exit()

				elif event.type == pg.KEYDOWN:
					self._check_keydown_events(event)

				elif event.type == pg.KEYUP:
					self._check_keyup_events(event)
					

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pg.K_RIGHT:
		# Move the ship to the right by one increment
			self.ship.moving_right =True

		elif event.key == pg.K_LEFT:
		# Move the ship to the left by one increment
			self.ship.moving_left =True

		elif event.key == pg.K_UP:
		# Move the ship to the up by one increment
			self.ship.moving_up =True

		elif event.key == pg.K_DOWN:
		# Move the ship to the up by one increment
			self.ship.moving_down =True

		elif event.key == pg.K_q:
			sys.exit()

		elif event.key == pg.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pg.K_RIGHT:
			self.ship.moving_right =False
		elif event.key == pg.K_LEFT:
			self.ship.moving_left =False
		elif event.key == pg.K_UP:
			self.ship.moving_up =False
		elif event.key == pg.K_DOWN:
			self.ship.moving_down =False
		

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = bl(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		# Update bullet positions.
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		# Make the most recently drawn sreen visible
		pg.display.flip()


if __name__ == '__main__':
   # Make a game instance, and run the game.
   ai = AlienInvasion()
   ai.run_game()

		