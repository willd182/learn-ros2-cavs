class SetSpeedManager:
    def __init__(self):
        # Initialize the set speed as 0 mph
        self._speed_mph = 0
        self.lower_limit_mph = 0
        self.upper_limit_mph = 65

    def set_speed(self, value):
        self._speed_mph = min(self.upper_limit_mph,
                              max(value, self.lower_limit_mph))

    @property
    def speed_mph(self):
        return self._speed_mph

    def increment_speed(self):
        self.set_speed(self.speed_mph + 5)

    def decrement_speed(self):
        self.set_speed(self.speed_mph - 5)
