import pygame

# Define a fonte
font = pygame.font.Font(None, 36)

def draw_button(screen, text, x, y, width, height, color, text_color, border_radius):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=border_radius)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)