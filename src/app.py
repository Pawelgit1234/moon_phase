import tkinter as tk
from moon_calculator import *
from coordinates import *


class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title("Moon phase calculator")
		self.geometry("400x600+720+200")
		self.resizable(width=False, height=False)
		# self.attributes('-topmost', True)

		latitude = get_coordinates_by_ip()[0]
		longitude = get_coordinates_by_ip()[1]
		moon_phase_percent = calculate_moon_phase(latitude, longitude, datetime.datetime.now())
		emoji_text = get_current_moon_emoji(moon_phase_percent)

		self.moon_emoji = tk.Label(self, text=emoji_text, font=('Helvetica', 150))
		self.moon_emoji.pack()
		self.phase_percent = tk.Label(self, text=str(round(moon_phase_percent, 2)) + '%', font=('Helvetica', 20))
		self.phase_percent.pack()
		self.latitude_and_longitude = tk.Label(self, text=f"Latitude: {latitude} | Longitude: {longitude}", font=('Helvetica', 10))
		self.latitude_and_longitude.pack()
		self.time = tk.Label(self, text=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), font=('Helvetica', 10))
		self.time.pack()
		self.city_name = tk.Label(self, text=get_city_name_by_ip(), font=('Helvetica', 20))
		self.city_name.pack()

		self.latitude_label = tk.Label(self, text="Latitude:")
		self.latitude_entry = tk.Entry(self)

		self.longitude_label = tk.Label(self, text="Longitude:")
		self.longitude_entry = tk.Entry(self)

		self.time_label = tk.Label(self, text="Date and Time (DD-MM-YYYY HH:MM:SS)")
		self.time_entry = tk.Entry(self)
		self.time_entry.insert(0, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

		self.calculate_button = tk.Button(self, text="Calculate", command=self.set_moon_phase)

		self.to_time_label = tk.Label(self, text="To time:")
		self.to_time_entry = tk.Entry(self)
		self.statistic_btn = tk.Button(self, text="Get Statistic", command=self.show_statistic)

		self.latitude_label.pack()
		self.latitude_entry.pack()

		self.longitude_label.pack()
		self.longitude_entry.pack()

		self.time_label.pack()
		self.time_entry.pack()

		self.calculate_button.pack()

		self.to_time_label.pack()
		self.to_time_entry.pack()

	def set_moon_phase(self):
		try:
			latitude = float(self.latitude_entry.get())
			longitude = float(self.longitude_entry.get())
			time_str = self.time_entry.get()
			time = datetime.datetime.strptime(time_str, "%d-%m-%Y %H:%M:%S")

			moon_phase_percent = calculate_moon_phase(latitude, longitude, time)
			emoji_text = get_current_moon_emoji(moon_phase_percent)

			self.moon_emoji.config(text=emoji_text)
			self.phase_percent.config(text=str(round(moon_phase_percent, 2)) + '%')
			self.latitude_and_longitude.config(text=f"Latitude: {latitude} | Longitude: {longitude}")
			self.time.config(text=time_str)
			self.city_name.config(text=get_city_name(latitude, longitude))
		except ValueError as e:
			self.phase_percent.config(text=str(e))

	def show_statistic(self):
		from_time = self.time_entry.get()
		to_time = self.to_time_entry.get()

