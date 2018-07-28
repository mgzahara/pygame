import pygame

def text_to_screen(screen, text, x, y, size = 15, color = (200, 0, 0)):
    text = str(text)
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
