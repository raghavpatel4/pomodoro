import tkinter as tk
from tkinter import ttk


class HomePage(ttk.Frame):
    def __init__(self, parent, start_callback):
        super().__init__(parent)
        self.start_callback = start_callback

        ttk.Label(self, text="Pomodoro Timer", font=("Arial", 18)).pack(pady=10)
        ttk.Label(self, text="Select number of Pomodoros:").pack(pady=5)

        self.pomodoro_count = tk.StringVar(value="4")
        pomodoro_spinbox = ttk.Spinbox(self, from_=1, to=10, textvariable=self.pomodoro_count, width=5)
        pomodoro_spinbox.pack(pady=5)

        ttk.Button(self, text="Start Session", command=self.start_session).pack(pady=10)

    def start_session(self):
        num_pomodoros = int(self.pomodoro_count.get())
        self.start_callback(num_pomodoros)


class TimerPage(ttk.Frame):
    def __init__(self, parent, timer, end_callback):
        super().__init__(parent)
        self.timer = timer
        self.end_callback = end_callback

        self.time_label = ttk.Label(self, text="25:00", font=("Arial", 36))
        self.time_label.pack(pady=10)

        self.state_label = ttk.Label(self, text="Pomodoro", font=("Arial", 18))
        self.state_label.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.start_pause_button = ttk.Button(self, text="Pause", command=self.toggle_timer)
        self.start_pause_button.pack(side="left", padx=10)

        self.stop_button = ttk.Button(self, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side="right", padx=10)

    def start_timer(self):
        self.timer.start()
        self.update_timer()

    def toggle_timer(self):
        if self.timer.is_running:
            self.timer.stop()
            self.start_pause_button.config(text="Resume")
        else:
            self.timer.start()
            self.start_pause_button.config(text="Pause")
            self.update_timer()

    def stop_timer(self):
        self.timer.stop()
        self.end_callback()

    def update_timer(self):
        if self.timer.is_running:
            self.timer.tick()
            self.time_label.config(text=self.timer.get_time_remaining())
            self.state_label.config(text=self.timer.get_current_state())

            if self.timer.current_state == "pomodoro":
                max_time = self.timer.POMODORO_TIME
            elif self.timer.current_state == "short_break":
                max_time = self.timer.SHORT_BREAK_TIME
            else:
                max_time = self.timer.LONG_BREAK_TIME

            progress = (max_time - self.timer.time_remaining) / max_time * 100
            self.progress_bar["value"] = progress

            self.after(1000, self.update_timer)
        else:
            self.start_pause_button.config(text="Start")