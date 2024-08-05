import tkinter as tk
from timer import Timer
from ui import HomePage, TimerPage, MenuPage


class PomodoroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.geometry("480x320")
        self.resizable(False, False)
        self.configure(bg="#ffffff")

        self.timer = Timer()

        # Create a frame to hold our pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.home_page = HomePage(self.container, self.start_session, self.show_help, self.show_menu_page)
        self.menu_page = MenuPage(self.container, self.start_timer)
        self.timer_page = TimerPage(self.container, self.timer, self.end_session)

        self.home_page.grid(row=0, column=0, sticky="nsew")
        self.timer_page.grid(row=0, column=0, sticky="nsew")

        self.show_home_page()

    def show_home_page(self):
        self.home_page.tkraise()

    def show_menu_page(self):
        print("Start button clicked")
        self.menu_page.tkraise()

    def show_help(self):
        print("Help button clicked")

    def show_timer_page(self):
        self.timer_page.tkraise()

    def start_session(self, num_pomodoros):
        self.timer.set_pomodoros(num_pomodoros)
        self.show_timer_page()
        self.timer_page.start_timer()

    def start_timer(self, num_pomodoros):
        self.timer.set_pomodoros(num_pomodoros)
        self.show_timer_page()
        self.timer_page.start_timer()

    def end_session(self):
        self.timer.reset()
        self.show_home_page()


if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()