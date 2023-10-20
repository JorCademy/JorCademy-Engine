from Components.Timer.timer import Timer

# Contains a dictionary of all timers in the game
timers: dict = {}


# Add a timer to the timer dictionary
def add_timer(name: str, duration: float) -> None:
    timers[name] = Timer(duration)


# Remove a timer from the timer dictionary
def remove_timer(name: str) -> None:
    timers.pop(name)


# Get a timer from the dictionary
def get_timer(name: str) -> Timer:
    return timers[name]


# Start a timer from the dictionary
def start_timer(name: str) -> None:
    timer = get_timer(name)
    if timer.finished:
        timer.start()


# Stop a timer from the dictionary
def stop_timer(name: str) -> None:
    timer = get_timer(name)
    timer.start()


# Pause timer from the dictionary
def toggle_pause_timer(name: str) -> None:
    timer = get_timer(name)
    timer.toggle_pause()


# Update timers
def update_timers() -> None:
    for timer in timers:
        timers[timer].update()
