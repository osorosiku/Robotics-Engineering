from __future__ import annotations

import sys

import pygame


WINDOW_WIDTH = 840
WINDOW_HEIGHT = 620
FPS = 60

BACKGROUND_COLOR = (18, 24, 38)
PANEL_COLOR = (28, 36, 56)
TEXT_COLOR = (235, 240, 250)
MUTED_COLOR = (150, 162, 186)
ACCENT_COLOR = (92, 162, 255)
WARNING_COLOR = (255, 189, 89)


def get_joystick() -> pygame.joystick.Joystick | None:
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        return None

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return joystick


def draw_text(surface: pygame.Surface, font: pygame.font.Font, text: str, x: int, y: int, color: tuple[int, int, int]) -> None:
    rendered = font.render(text, True, color)
    surface.blit(rendered, (x, y))


def draw_bar(surface: pygame.Surface, rect: pygame.Rect, value: float, color: tuple[int, int, int]) -> None:
    pygame.draw.rect(surface, (52, 62, 88), rect, border_radius=10)

    normalized = max(-1.0, min(1.0, value))
    filled_width = int(rect.width * abs(normalized))
    if normalized >= 0:
      filled_rect = pygame.Rect(rect.x, rect.y, filled_width, rect.height)
    else:
      filled_rect = pygame.Rect(rect.right - filled_width, rect.y, filled_width, rect.height)

    if filled_width > 0:
        pygame.draw.rect(surface, color, filled_rect, border_radius=10)

    center_x = rect.centerx
    pygame.draw.line(surface, (220, 226, 240), (center_x, rect.top), (center_x, rect.bottom), 1)


def main() -> None:
    pygame.init()
    pygame.joystick.init()
    pygame.display.set_caption("Joystick Monitor")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("meiryo", 30, bold=True)
    body_font = pygame.font.SysFont("meiryo", 22)
    small_font = pygame.font.SysFont("meiryo", 18)

    joystick = get_joystick()
    axis_count = joystick.get_numaxes() if joystick else 0
    button_count = joystick.get_numbuttons() if joystick else 0
    hat_count = joystick.get_numhats() if joystick else 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if joystick is None:
            joystick = get_joystick()
            if joystick is not None:
                axis_count = joystick.get_numaxes()
                button_count = joystick.get_numbuttons()
                hat_count = joystick.get_numhats()

        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, PANEL_COLOR, pygame.Rect(28, 28, WINDOW_WIDTH - 56, WINDOW_HEIGHT - 56), border_radius=24)

        draw_text(screen, title_font, "Joystick Monitor", 50, 48, TEXT_COLOR)
        draw_text(screen, small_font, "Move sticks and press buttons to see live values.", 50, 88, MUTED_COLOR)

        if joystick is None:
            draw_text(screen, body_font, "ジョイスティックを接続してください。", 50, 150, WARNING_COLOR)
            draw_text(screen, small_font, "接続後は自動で再検出します。", 50, 182, MUTED_COLOR)
            pygame.display.flip()
            clock.tick(FPS)
            continue

        draw_text(screen, small_font, f"Device: {joystick.get_name()}", 50, 138, TEXT_COLOR)
        draw_text(screen, small_font, f"Axes: {axis_count}  Buttons: {button_count}  Hats: {hat_count}", 50, 164, MUTED_COLOR)

        top = 212

        draw_text(screen, body_font, "Axes", 50, top, ACCENT_COLOR)
        top += 36
        for axis_index in range(axis_count):
            axis_value = joystick.get_axis(axis_index)
            draw_text(screen, small_font, f"Axis {axis_index}", 52, top + axis_index * 42 + 4, TEXT_COLOR)
            bar_rect = pygame.Rect(150, top + axis_index * 42, 420, 24)
            draw_bar(screen, bar_rect, axis_value, ACCENT_COLOR)
            draw_text(screen, small_font, f"{axis_value:+.3f}", 590, top + axis_index * 42 + 2, TEXT_COLOR)

        buttons_top = top + max(axis_count, 1) * 42 + 24
        draw_text(screen, body_font, "Buttons", 50, buttons_top, ACCENT_COLOR)
        buttons_top += 36

        columns = 8
        for button_index in range(button_count):
            button_value = joystick.get_button(button_index)
            column = button_index % columns
            row = button_index // columns
            x = 52 + column * 92
            y = buttons_top + row * 42

            circle_color = (74, 88, 120) if button_value == 0 else WARNING_COLOR
            pygame.draw.circle(screen, circle_color, (x + 10, y + 10), 10)
            draw_text(screen, small_font, f"{button_index}: {button_value}", x + 26, y - 1, TEXT_COLOR)

        hats_top = buttons_top + ((button_count + columns - 1) // columns) * 42 + 24
        draw_text(screen, body_font, "Hats", 50, hats_top, ACCENT_COLOR)
        hats_top += 36

        if hat_count == 0:
            draw_text(screen, small_font, "Hat input is not available on this controller.", 50, hats_top, MUTED_COLOR)
        else:
            for hat_index in range(hat_count):
                hat_value = joystick.get_hat(hat_index)
                draw_text(screen, small_font, f"Hat {hat_index}: {hat_value}", 52, hats_top + hat_index * 30, TEXT_COLOR)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()