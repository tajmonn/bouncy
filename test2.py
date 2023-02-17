import pygame
from classes.classBall import Ball

# Initialize pygame
pygame.init()
ball = Ball()

# Set window size
window_width = 1920
window_height = 1080

# Set frame size and position
frame_width = 400
frame_height = 400
frame_x = (window_width - frame_width) / 2
frame_y = (window_height - frame_height) / 2

# Set ball properties
# ball_radius = 10
# ball_x = 400
# ball_y = 300
# ball_velocity_x = 2
# ball_velocity_y = 2

# Set framerate
framerate = 60

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Create window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ball inside frame")

# Create clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            frame_x = mouse_x - frame_width / 2
            frame_y = mouse_y - frame_height / 2

    # Check if the ball is hitting the left or right walls of the frame
    if ball.x + ball.radius > frame_x + frame_width:
        if ball.x + ball.radius - frame_x - frame_width > 10:
            ball.gain_speed("left")
        ball.velocity_x = -abs(ball.velocity_x)
        ball.x = frame_x + frame_width - ball.radius
        
    elif ball.x - ball.radius < frame_x:
        if ball.x - ball.radius - frame_x < -10:
            ball.gain_speed("right")
        ball.velocity_x = abs(ball.velocity_x)
        ball.x = frame_x + ball.radius
        

    # Check if the ball is hitting the top or bottom walls of the frame
    if ball.y + ball.radius > frame_y + frame_height:
        if ball.y + ball.radius - frame_y - frame_height > 10:
            ball.gain_speed("down")
        ball.velocity_y = -abs(ball.velocity_y)
        ball.y = frame_y + frame_height - ball.radius
        
    elif ball.y - ball.radius < frame_y:
        if ball.y - ball.radius - frame_y < -10:
            ball.gain_speed("up")
        ball.velocity_y = abs(ball.velocity_y)
        ball.y = frame_y + ball.radius
        
    # Update the position of the ball
    ball.x += ball.velocity_x
    ball.y += ball.velocity_y
    ball.lose_speed()
    print(ball.velocity_x, ball.velocity_y)
    # Clear the screen
    screen.fill(white)

    # Draw the frame
    pygame.draw.rect(screen, black, (frame_x, frame_y, frame_width, frame_height), 5)

    # Draw the ball
    pygame.draw.circle(screen, red, (int(ball.x), int(ball.y)), ball.radius, 0)

    # Update the screen
    pygame.display.update()

    # Set the framerate
    clock.tick(framerate)

# Quit pygame
pygame.quit()
