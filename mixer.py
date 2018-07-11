import pygame, time

pygame.init()
pygame.mixer.init()

sound1 = pygame.mixer.Sound('Garden Music.mp3')
sound2 = pygame.mixer.Sound('Floating Cities.mp3')
sound1.play(loops=-1,fade_ms=1000)

time.sleep(10)

sound1.fadeout(1000)
sound2.play(loops=-1,fade_ms=1000)


# Test if this works plz :)
