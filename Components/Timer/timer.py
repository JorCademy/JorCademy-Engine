from Components.Support.settings import delta_time


class Timer:

    def __init__(self, duration: float):
        self.duration = duration
        self.time = 0.0
        self.finished = False
        self.paused = False

    def update(self) -> None:
        if self.paused:
            return

        self.time += delta_time

        if self.time >= self.duration:
            self.finished = True
            self.time = 0.0

    def toggle_pause(self) -> None:
        self.paused = not self.paused

    def start(self) -> None:
        self.time = 0.0
        self.finished = False
