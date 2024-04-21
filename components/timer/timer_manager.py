from components.timer.timer import Timer

# Contains a dictionary of all timers in the game
timers: dict = {}


def add_timer(name: str, duration: float) -> None:
    """
    Add a timer to the timer dictionary

    :param name: Name of the timer
    :param duration: Duration of the timer
    :return: None
    """
    timers[name] = Timer(duration)


def remove_timer(name: str) -> None:
    """
    Remove a timer from the dictionary

    :param name: Name of the timer
    :return: None
    """
    timers.pop(name)


def get_timer(name: str) -> Timer:
    """
    Get a timer from the dictionary

    :param name: Name of the timer
    :return: timer
    """
    return timers[name]


def start_timer(name: str) -> None:
    """
    Start a timer from the dictionary

    :param name: Name of the timer
    :return: None
    """
    timer = get_timer(name)
    if timer.finished:
        timer.start()


def stop_timer(name: str) -> None:
    """
    Stop a timer from the dictionary

    :param name: Name of the timer
    :return: None
    """
    timer = get_timer(name)
    timer.start()


def toggle_pause_timer(name: str) -> None:
    """
    Toggle the pause state of a timer

    :param name: Name of the timer
    :return: None
    """
    timer = get_timer(name)
    timer.toggle_pause()


# Update timers
def update_timers() -> None:
    """
    Update all timers

    :return: None
    """
    for timer in timers:
        timers[timer].update()
