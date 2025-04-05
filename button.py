import pygame
from typing import Tuple, Optional

class Button:
    def __init__(self, color: Tuple[int, int, int], x: int, y: int, width: int, height: int, text: str = ''):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self, surface: pygame.Surface, outline_color: Optional[Tuple[int, int, int]] = None) -> None:
        """Draw a nice-looking button with hover effect and optional outline."""
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.is_over(mouse_pos)



        # Outline
        if outline_color:
            outline_rect = self.rect.inflate(4, 4)
            pygame.draw.rect(surface, outline_color, outline_rect, border_radius=12)

        # Hover effect color
        draw_color = tuple(min(255, c + 30) if is_hovered else c for c in self.color)
        pygame.draw.rect(surface, draw_color, self.rect, border_radius=12)

        # Optional text shadow
        if self.text:
            shadow = self.font.render(self.text, True, (50, 50, 50))
            shadow_rect = shadow.get_rect(center=(self.rect.centerx + 2, self.rect.centery + 2))
            surface.blit(shadow, shadow_rect)

            # Draw actual text
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def is_over(self, pos: Tuple[int, int]) -> bool:
        """Return True if mouse is over the button."""
        return self.rect.collidepoint(pos)
