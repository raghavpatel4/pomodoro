import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class HomePage(ttk.Frame):
    def __init__(self, parent, start_callback, help_callback, menu_callback):
        super().__init__(parent)
        self.parent = parent
        self.start_callback = start_callback
        self.help_callback = help_callback
        self.menu_callback = menu_callback

        self.background_label = tk.Label(self)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.after(100, self.load_title_screen)  # Short delay to ensure window is rendered

        self.canvas = tk.Canvas(self, width=480, height=320, bd=0, highlightthickness=0)
        self.canvas.pack()

        self.pomodoro_count = tk.StringVar(value="4")
        #self.pomodoro_spinbox = ttk.Spinbox(self, from_=1, to=10, textvariable=self.pomodoro_count, width=5)
        #self.start_button = ttk.Button(self, text="Start Session", command=self.start_session)

        # We'll position these widgets after loading the background

    def load_title_screen(self):
        self.update()  # Force an update of the widget tree
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        print(f"Home Window size: {window_width}x{window_height}")  # Debug print

        if window_width <= 1 or window_height <= 1:
            # If correct dimensions are not available, retry after a short delay
            self.after(100, self.load_title_screen())
            return

        try:
            bg = Image.open("assets/graphics/title_screen.png")
            bg = bg.resize((window_width, window_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(bg)
            self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')

            # Load the button images
            start_btn = Image.open("assets/graphics/start_btn.png")
            help_btn = Image.open("assets/graphics/help_btn.png")

            # Get button dimensions
            start_btn_width, start_btn_height = start_btn.size
            help_btn_width, help_btn_height = help_btn.size

            # Resize button images to enlarge by 1.5
            start_btn = start_btn.resize((int(start_btn_width * 1.5), int(start_btn_height * 1.5)))
            help_btn = help_btn.resize((int(help_btn_width * 1.5), int(help_btn_height * 1.5)))

            # Create the buttons
            self.start_btn_image = ImageTk.PhotoImage(start_btn)
            self.help_btn_image = ImageTk.PhotoImage(help_btn)
            self.start_btn = self.canvas.create_image(240, 140, image=self.start_btn_image, anchor='center')
            self.help_btn = self.canvas.create_image(240, 172, image=self.help_btn_image, anchor='center')

            # Bind the buttons to their respective callbacks
            self.canvas.tag_bind(self.start_btn, "<Button-1>", lambda e: self.menu_callback())
            self.canvas.tag_bind(self.help_btn, "<Button-1>", lambda e: self.help_callback())

        except Exception as e:
            print(f"Error loading image: {e}")

    def help_callback(self):
        print("Help button clicked")

    def show_menu_callback(self):
        print("Menu button clicked")
        self.show_menu_callback()


class MenuPage(ttk.Frame):
    def __init__(self, parent, start_timer_callback):
        super().__init__(parent)
        self.start_timer_callback = start_timer_callback

        self.background_label = tk.Label(self)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.after(100, self.load_menu_screen)  # Short delay to ensure window is rendered

        self.canvas = tk.Canvas(self, width=480, height=320, bd=0, highlightthickness=0)
        self.canvas.pack()

        print("Inside MenuPage")

    def load_menu_screen(self):
        self.update()  # Force an update of the widget tree
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        print(f"Menu Window size: {window_width}x{window_height}")  # Debug print

        if window_width <= 1 or window_height <= 1:
            # If correct dimensions are not available, retry after a short delay
            self.after(100, self.load_menu_screen)
            return

        try:
            bg = Image.open("assets/graphics/bg.png")
            bg = bg.resize((window_width, window_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(bg)
            self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')

            # Load the button images
            start_btn = Image.open("assets/graphics/start_btn.png")
            help_btn = Image.open("assets/graphics/help_btn.png")

            # Get button dimensions
            start_btn_width, start_btn_height = start_btn.size
            help_btn_width, help_btn_height = help_btn.size

            # Resize button images to enlarge by 1.5
            start_btn = start_btn.resize((int(start_btn_width * 1.5), int(start_btn_height * 1.5)))
            help_btn = help_btn.resize((int(help_btn_width * 1.5), int(help_btn_height * 1.5)))

            # Create the buttons
            self.start_btn_image = ImageTk.PhotoImage(start_btn)
            self.help_btn_image = ImageTk.PhotoImage(help_btn)
            self.start_btn = self.canvas.create_image(240, 140, image=self.start_btn_image, anchor='center')
            self.help_btn = self.canvas.create_image(240, 172, image=self.help_btn_image, anchor='center')


            # Bind the buttons to their respective callbacks
            self.canvas.tag_bind(self.start_btn, "<Button-1>", lambda e: self.menu_callback())
            self.canvas.tag_bind(self.help_btn, "<Button-1>", lambda e: self.help_callback())

        except Exception as e:
            print(f"Error loading image: {e}")

    def start_timer(self):
        num_pomodoros = int(self.pomodoro_count.get())
        self.start_callback(num_pomodoros)


class TimerPage(ttk.Frame):
    def __init__(self, parent, timer, end_callback):
        super().__init__(parent)
        self.timer = timer
        self.end_callback = end_callback

        self.background_label = tk.Label(self)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.after(100, self.load_timer_screen())

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

    def load_timer_screen(self):
        self.update()  # Force an update of the widget tree
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        print(f"Timer Window size: {window_width}x{window_height}")  # Debug print

        if window_width <= 1 or window_height <= 1:
            # If we still don't have the correct size, try again after a short delay
            self.after(100, self.load_timer_screen)
            return

        try:
            img = Image.open("assets/graphics/bg.png")
            img = img.resize((window_width, window_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(img)
            self.background_label.config(image=self.background_image)

            # Now that we have the background, let's position our widgets
            self.pomodoro_spinbox.place(relx=0.5, rely=0.7, anchor='center')
            self.start_button.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            print(f"Error loading image: {e}")