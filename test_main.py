import pygame
from classes.classBall import Ball
from classes.classFrame import Frame
from functions.defs import calculate_speed, calculate_friction
from configs.loader import game_settings

# TODO -> tidy up somehow functions and functions\defs.py
# TODO -> add gravitation for the ball
# TODO -> start making class for spike/lava/ground-wall
# TODO -> tidy up the code in general (make hitting the frame's walls smarter)

pts = game_settings["power_to_speed"]
fr = game_settings["friction"]
bi = game_settings["border_interaction"]
window_width = game_settings["window_width"]
window_height = game_settings["window_height"]
framerate = game_settings["framerate"]
background = pygame.image.load("images/bg.jpg")
icon = pygame.image.load("images/icon.png")


# Initialize pygame
pygame.init()
ball = Ball()
frame = Frame()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Your mother: THE GAME")
pygame.mouse.set_visible(False)
pygame.display.set_icon(icon)
pause_text = pygame.font.SysFont("Arial", 32).render(
    "Pause", True, pygame.color.Color("White")
)
clock = pygame.time.Clock()
RUNNING, PAUSE = 0, 1
state = RUNNING


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            frame.change_pos(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == PAUSE:
                    state = RUNNING
                else:
                    state = PAUSE

    else:
        #! STATE RUNNING
        if state == RUNNING:
            # Check if the ball is hitting the left or right walls of the frame
            if ball.x + ball.radius > frame.x + frame.width:
                if (
                    ball.x + ball.radius - frame.x - frame.width > bi
                    and frame.power_x < 0
                ):
                    ball.gain_speed(
                        "horizontal",
                        calculate_speed(frame.power_x, pts),
                        calculate_friction(frame.power_y, fr),
                    )

                ball.velocity_x *= -1
                ball.x = frame.x + frame.width - ball.radius

            elif ball.x - ball.radius < frame.x:
                if ball.x - ball.radius - frame.x < -bi and frame.power_x > 0:
                    ball.gain_speed(
                        "horizontal",
                        calculate_speed(frame.power_x, pts),
                        calculate_friction(frame.power_y, fr),
                    )
                ball.velocity_x *= -1
                ball.x = frame.x + ball.radius

            # Check if the ball is hitting the top or bottom walls of the frame
            if ball.y + ball.radius > frame.y + frame.height:
                if (
                    ball.y + ball.radius - frame.y - frame.height > bi
                    and frame.power_y < 0
                ):
                    ball.gain_speed(
                        "vertical",
                        calculate_speed(frame.power_y, pts),
                        calculate_friction(frame.power_x, fr),
                    )
                ball.velocity_y *= -1
                ball.y = frame.y + frame.height - ball.radius

            elif ball.y - ball.radius < frame.y:
                if ball.y - ball.radius - frame.y < -bi and frame.power_y > 0:
                    ball.gain_speed(
                        "vertical",
                        calculate_speed(frame.power_y, pts),
                        calculate_friction(frame.power_x, fr),
                    )
                ball.velocity_y *= -1
                ball.y = frame.y + ball.radius

            # * Update the position of the ball
            ball.x += ball.velocity_x
            ball.y += ball.velocity_y
            # * Drawing everything
            screen.blit(background, (0, 0))
            pygame.draw.rect(
                screen, frame.color, (frame.x, frame.y, frame.width, frame.height), 5
            )
            pygame.draw.circle(
                screen, ball.color, (int(ball.x), int(ball.y)), ball.radius, 0
            )
            # * After everything is drawn
            frame.zero_the_power()
            ball.lose_speed()

        #! STATE PAUSE
        elif state == PAUSE:
            screen.blit(pause_text, (900, 520))

    pygame.display.update()
    clock.tick(framerate)

# ? Quit pygame
pygame.quit()
