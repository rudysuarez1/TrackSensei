import time

from . import config, gps_functions


def main():
    gps_reader = gps_functions.read_gps_data()
    for lat, lon in gps_reader:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - Latitude: {lat}, Longitude: {lon}")


if __name__ == "__main__":
    main()
