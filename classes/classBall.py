class Ball:
    def __init__(self):
        self.radius = 10
        self.x = 400
        self.y = 300
        self.velocity_x = 0
        self.velocity_y = 0
        self.color = (255, 0, 0)  #!red
        self.max_speed = 15
        self.speed_falloff = 89 / 90

    def gain_speed(self, direction):
        match direction:
            case "left":
                self.velocity_x = -self.max_speed
            case "right":
                self.velocity_x = self.max_speed
            case "up":
                self.velocity_y = self.max_speed
            case "down":
                self.velocity_y = -self.max_speed

    def lose_speed(self):
        self.velocity_x = self.velocity_x * self.speed_falloff
        self.velocity_y = self.velocity_y * self.speed_falloff
        # if self.velocity_x < .001:
        #     self.velocity_x = 0
        # if self.velocity_y < .001:
        #     self.velocity_y = 0
