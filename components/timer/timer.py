from components.support.settings import delta_time


class Timer:
    """
    A timer
    """

    def __init__(self, duration: float) -> None:
        self.duration = duration
        self.time = 0.0
        self.finished = False
        self.paused = False

    def update(self) -> None:
        """
        Update the timer

        :return: None
        """
        if self.paused:
            return

        self.time += delta_time

        if self.time >= self.duration:
            self.finished = True
            self.time = 0.0

    def toggle_pause(self) -> None:
        """
        Toggle the pause state of the timer

        :return: None
        """
        self.paused = not self.paused

    def start(self) -> None:
        """
        Start the timer

        :return: None
        """
        self.time = 0.0
        self.finished = False
