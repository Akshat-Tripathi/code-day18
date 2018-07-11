import pygame, time

pygame.init()
pygame.mixer.init()

sound1 = pygame.mixer.Sound('Garden Music.mp3')
sound2 = pygame.mixer.Sound('Floating Cities.mp3')
channel1 = pygame.mixer.Channel(1)
channel2 = pygane.mixer.Channel(2)
channel1.play(sound1,loops=-1,fade_ms=1000)

time.sleep(20)

channel1.fadeout(1000)
channel1.play(loops=-1,fade_ms=1000)


# Test if this works plz :)
