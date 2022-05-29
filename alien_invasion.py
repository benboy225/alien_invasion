""" We will now create an empty game window using pygame. the objective here is to then add 
the other parts of the game later."""

import sys

import pygame as pg

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initialize the game, and create game resources."""
		pg.init()
		
		self.screen = pg.display.set_mode((1200, 800))
		pg.display.set_caption("Alien Invasion") #this is called surface

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			# Watch for keyboard and mouse events
			for event in pg.event.get():
				if event.type == pg.QUIT:
					sys.exit()


			# Make the most recently drawn sreen visible
			pg.display.flip()

if __name__ == '__main__':
   # Make a game instance, and run the game.
   ai = AlienInvasion()
   ai.run_game()

		