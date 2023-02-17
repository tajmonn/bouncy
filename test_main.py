import pygame
from classes.classBall import Ball
from classes.classFrame import Frame
from functions.defs import calculate_speed, calculate_friction
from configs.loader import game_settings

# Initialize pygame
pygame.init()
ball = Ball()
pts = game_settings["power_to_speed"]
fr = game_settings["friction"]
bi = game_settings["border_interaction"]
# Set window size
window_width = game_settings["window_width"]
window_height = game_settings["window_height"]
frame = Frame()

# Set framerate
framerate = game_settings["framerate"]

# Set background colors
background = pygame.image.load("images/bg.jpg")

# Create window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ball inside frame")
pygame.mouse.set_visible(False)

# Create clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Update the position of the ball
    ball.x += ball.velocity_x
    ball.y += ball.velocity_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            frame.change_pos(event.pos)

    # Check if the ball is hitting the left or right walls of the frame
    if ball.x + ball.radius > frame.x + frame.width:
        if ball.x + ball.radius - frame.x - frame.width > bi and frame.power_x < 0:
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
        if ball.y + ball.radius - frame.y - frame.height > bi and frame.power_y < 0:
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

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw the frame
    pygame.draw.rect(
        screen, frame.color, (frame.x, frame.y, frame.width, frame.height), 5
    )

    # Draw the ball
    pygame.draw.circle(screen, ball.color, (int(ball.x), int(ball.y)), ball.radius, 0)

    # Update the screen
    pygame.display.update()

    frame.zero_the_power()
    # Set the framerate
    ball.lose_speed()

    clock.tick(framerate)

# Quit pygame
pygame.quit()
