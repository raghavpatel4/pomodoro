import tkinter as tk
from timer import Timer
from ui import HomePage, TimerPage


class PomodoroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.geometry("300x200")
        self.resizable(False, False)

        self.timer = Timer()
        self.home_page = HomePage(self, self.start_session)
        self.timer_page = TimerPage(self, self.timer, self.end_session)

        self.show_home_page()

    def show_home_page(self):
        self.timer_page.pack_forget()
        self.home_page.pack()

    def show_timer_page(self):
        self.home_page.pack_forget()
        self.timer_page.pack()

    def start_session(self, num_pomodoros):
        self.timer.set_pomodoros(num_pomodoros)
        self.show_timer_page()
        self.timer_page.start_timer()

    def end_session(self):
        self.timer.reset()
        self.show_home_page()


if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()