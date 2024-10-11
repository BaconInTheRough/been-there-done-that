import tkinter as tk
import plotly.express as px
import pandas as pd
import json


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello World")

        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate window size (e.g., 50% of screen size)
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)

        # Calculate position for center of the screen
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the window size and position
        self.geometry(
            f"{window_width}x{window_height}+{position_right}+{position_top}"
            )

        df = json.loads('{"country": "Canada"}')

        map = px.choropleth(locations='iso_a3', 
                    color='gdp_md_est',
                    projection='natural earth'
                    )

        map.show()

        self.map_widget = tk.Label(self,
                                   width=window_width,
                                   height=window_height,
                                #    image=map
                                   )

        self.map_widget.pack(expand=True)

    def run(self):
        self.mainloop()

    def stop(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.run()
