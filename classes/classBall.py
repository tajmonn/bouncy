from configs.loader import ball_settings


class Ball:
    def __init__(self):
        self.radius = ball_settings["radius"]
        self.x = ball_settings["start_x"]
        self.y = ball_settings["start_y"]
        self.velocity_x = 0
        self.velocity_y = 0
        self.color = ball_settings["color"]
        self.speed_falloff = ball_settings["speed_falloff"]
        self.max_speed = ball_settings["max_speed"]

    def limiting(self):
        if self.velocity_x > self.max_speed or self.velocity_x < -self.max_speed:
            if self.max_speed < 0:
                self.velocity_x = -self.max_speed
            else:
                self.velocity_x = self.max_speed
        elif self.velocity_y > self.max_speed or self.velocity_y < -self.max_speed:
            if self.max_speed < 0:
                self.velocity_y = -self.max_speed
            else:
                self.velocity_y = self.max_speed

    def gain_speed(self, direction, speed, friction):
        match direction:
            case "horizontal":
                self.velocity_x -= speed
                self.velocity_y += friction
            case "vertical":
                self.velocity_y -= speed
                self.velocity_x += friction
        self.limiting()

    def lose_speed(self):
        self.velocity_x = (
            self.velocity_x * self.speed_falloff[0] / self.speed_falloff[1]
        )
        self.velocity_y = (
            self.velocity_y * self.speed_falloff[0] / self.speed_falloff[1]
        )
