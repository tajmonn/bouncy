from configs.loader import frame_settings


class Frame:
    def __init__(self):
        self.width = frame_settings["width"]
        self.height = frame_settings["height"]
        self.x = frame_settings["start_x"]
        self.y = frame_settings["start_y"]
        self.color = frame_settings["color"]
        self.speed = 0
        self.power_x = 0
        self.power_y = 0

    def change_pos(self, new_pos):
        self.power_x += new_pos[0] - self.width / 2 - self.x
        self.power_y += new_pos[1] - self.height / 2 - self.y
        self.x = new_pos[0] - self.width / 2
        self.y = new_pos[1] - self.height / 2

    def zero_the_power(self):
        self.power_x = 0
        self.power_y = 0
