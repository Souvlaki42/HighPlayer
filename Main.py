import pygame, sys

display_size = (400,400)

pygame.init()
pygame.mixer.init()
pygame.display.set_mode(display_size)



sound0 = pygame.mixer.Sound("sounds/sound0.wav")
sound1 = pygame.mixer.Sound("sounds/sound1.wav")
sound2 = pygame.mixer.Sound("sounds/sound2.wav")
sound3 = pygame.mixer.Sound("sounds/sound3.wav")
sound4 = pygame.mixer.Sound("sounds/sound4.wav")
sound5 = pygame.mixer.Sound("sounds/sound5.wav")
sound6 = pygame.mixer.Sound("sounds/sound6.wav")
sound7 = pygame.mixer.Sound("sounds/sound7.wav")
sound8 = pygame.mixer.Sound("sounds/sound8.wav")
sound9 = pygame.mixer.Sound("sounds/sound9.wav")

def stopSounds():
	sound0.stop()
	sound1.stop()
	sound2.stop()
	sound3.stop()
	sound4.stop()
	sound5.stop()
	sound6.stop()
	sound7.stop()
	sound8.stop()
	sound9.stop()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_0:
				stopSounds()
				sound0.play()
			if event.key == pygame.K_1:
				stopSounds()
				sound1.play()
			if event.key == pygame.K_2:
				stopSounds()
				sound2.play()
			if event.key == pygame.K_3:
				stopSounds()
				sound3.play()
			if event.key == pygame.K_4:
				stopSounds()
				sound4.play()
			if event.key == pygame.K_5:
				stopSounds()
				sound5.play()
			if event.key == pygame.K_6:
				stopSounds()
				sound6.play()
			if event.key == pygame.K_7:
				stopSounds()
				sound7.play()
			if event.key == pygame.K_8:
				stopSounds()
				sound8.play()
			if event.key == pygame.K_9:
				stopSounds()
				sound9.play()