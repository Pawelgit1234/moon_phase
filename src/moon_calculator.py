import ephem
import datetime


def get_current_moon_emoji(percent: float) -> str:
	if percent > 100.0:
		raise RuntimeError("Percent can not be bigger than 100%")

	emojis = ["🌑", "🌒", "🌓", "🌔", "🌕"]
	i = int(percent // 20)
	return emojis[i]


def calculate_moon_phase(latitude: float, longitude: float, time: datetime.datetime) -> float:
	observer = ephem.Observer()
	observer.lat = str(latitude)
	observer.lon = str(longitude)
	observer.date = time
	moon = ephem.Moon()
	moon.compute(observer)

	return moon.phase