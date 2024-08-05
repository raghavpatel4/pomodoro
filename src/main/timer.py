import time


class Timer:
    POMODORO_TIME = 25 * 60  # 25 minutes
    SHORT_BREAK_TIME = 5 * 60  # 5 minutes
    LONG_BREAK_TIME = 30 * 60  # 30 minutes

    def __init__(self):
        self.total_pomodoros = 0
        self.current_pomodoros = 0
        self.time_remaining = 0
        self.is_running = False
        self.current_state = "pomodoro"

    def set_pomodoros(self, num_pomodoros):
        self.total_pomodoros = num_pomodoros
        self.current_pomodoros = 1
        self.time_remaining = self.POMODORO_TIME

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def reset(self):
        self.__init__()
        #self.total_pomodoros = 0
        #self.current_pomodoros = 0
        #self.time_remaining = 0
        #self.is_running = False
        #self.current_state = "pomodoro"

    def tick(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
        elif self.time_remaining == 0:
            self.next_state()

    def next_state(self):
        if self.current_state == "pomodoro":
            if self.current_pomodoros % 4 == 0:
                self.current_state = "long_break"
                self.time_remaining = self.LONG_BREAK_TIME
            else:
                self.current_state = "short_break"
                self.time_remaining = self.SHORT_BREAK_TIME
        else:
            if self.current_pomodoros < self.total_pomodoros:
                self.current_pomodoros += 1
                self.current_state = "pomodoro"
                self.time_remaining = self.POMODORO_TIME
            else:
                self.is_running = False

    def get_time_remaining(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        return f"{minutes:02}:{seconds:02}"

    def get_current_state(self):
        return self.current_state
