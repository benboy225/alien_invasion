""" We will now create an empty game window using pygame. the objective here is to then add 
the other parts of the game later."""

import sys

import pygame as pg

from settings import Settings as st

from ship import Ship as sp

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initialize the game, and create game resources."""
		pg.init()

		self.settings = st()
		
		self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height,))
		pg.display.set_caption("Alien Invasion") #this is called surface

		self.ship = sp(self)

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			# Watch for keyboard and mouse events
			self._check_events()
			self.ship.update()

			# redraw the screen during each pass through the loop
			self._update_screen()


			# Make the most recently drawn sreen visible
			pg.display.flip()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pg.event.get():
				if event.type == pg.QUIT:
					sys.exit()

				elif event.type == pg.KEYDOWN:
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

				elif event.type == pg.KEYUP:
					if event.key == pg.K_RIGHT:
						self.ship.moving_right =False
					elif event.key == pg.K_LEFT:
						self.ship.moving_left =False
					elif event.key == pg.K_UP:
						self.ship.moving_up =False
					elif event.key == pg.K_DOWN:
						self.ship.moving_down =False


	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

if __name__ == '__main__':
   # Make a game instance, and run the game.
   ai = AlienInvasion()
   ai.run_game()

		