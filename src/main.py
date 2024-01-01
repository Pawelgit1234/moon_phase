import ephem
import datetime


def moon_phase(latitude: float, longitude: float, time: datetime.datetime) -> float:
	observer = ephem.Observer()
	observer.lat = str(latitude)
	observer.lon = str(longitude)
	observer.date = time
	moon = ephem.Moon()
	moon.compute(observer)

	return moon.phase


if __name__ == "__main__":
	latitude = 6.983333
	longitude = 51.033333

	custom_time = datetime.datetime(2024, 1, 2, 0, 31, 0)

	current_phase_percentage = moon_phase(latitude, longitude, custom_time)
	print(f"Текущая фаза луны в процентах для координат ({latitude}, {longitude}):", round(current_phase_percentage, 2), "%")
