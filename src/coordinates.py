import requests
from geopy.geocoders import Nominatim


def get_coordinates_by_ip() -> tuple:
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        coordinates = data.get('loc', '').split(',')
        latitude, longitude = map(float, coordinates)
        return latitude, longitude
    except Exception as e:
        print(f"Error with coordinates: {e}")
        return None


def get_city_name_by_ip() -> str:
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get('city')
        return city
    except Exception as e:
        print(f"Error with coordinates: {e}")
        return None


def get_city_name(latitude: float, longitude: float) -> str:
    geolocator = Nominatim(user_agent="moon_phase")
    location = geolocator.reverse(f"{latitude}, {longitude}", language="eng")
    address = location.address
    city_name = address.split(",")[-3]
    return city_name.strip()
