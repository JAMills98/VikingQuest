# V1 Code: This doesnt have any gameplay, just fundamentals of time
import pygame
from pygame.locals import *
pygame.init()
FLAGS = FULLSCREEN | DOUBLEBUF
SCREEN = pygame.display.set_mode((0,0), 0)
RUNNING = 1

CLOCK = pygame.time.Clock()
FRAMECOUNT = 0
FPS_MAX = 30

# MAGIC HACK: Pygame doesnt have Event Timestamps, so our closest solution is to set a Timer to create events BETWEEN Frames
pygame.time.set_timer(USEREVENT, 100)


while RUNNING:

	
	DELTA = CLOCK.get_time()
	
	
	# Do all buffered events ASSUMING equal timeframes
	EVENT_QUEUE = pygame.event.get()
	
	if EVENT_QUEUE:
		print(EVENT_QUEUE)
		for event in EVENT_QUEUE:
			if event.type == QUIT:
				pygame.quit()
			
			if event.type == KEYDOWN:
				# EXIT on ALTF4
				if event.mod == KMOD_LALT and event.key == K_F4:
						pygame.quit()
					

	
	#print("Frame #",FRAMECOUNT,"DELTA=",DELTA)
	# Game needs to Simulate Stuff for DELTATIME
	
	FRAMECOUNT+=1
	CLOCK.tick(FPS_MAX)
